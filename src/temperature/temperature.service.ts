import { Inject, Injectable } from '@nestjs/common';
import { PrismaService } from 'src/db/prisma.service';
import { GetGroupedDataDto, GROUPBY } from './dto/get-temperature.dto';
import { ClientProxy } from '@nestjs/microservices';
import { groupByDate } from 'src/utils/group-data.util';
import { GetConsumptionLastDto } from 'src/consumtion/dto/get-consumtion-last.dto';
import { HttpService } from '@nestjs/axios';

// Define a type for the grouped data
export interface GroupedData<T> {
  content: T[];
  sum: number;
  count: number;
}
export interface AiTemperaturePrediction {
  predicted_temperature: number;
  humidity: number;
}

@Injectable()
export class TemperatureService {
  constructor(
    private readonly prisma: PrismaService,
    @Inject('ALERT_SERVICE') private readonly alertService: ClientProxy,
    private readonly httpService: HttpService,
  ) {}

  clearTemperatureEntries(companyId: string) {
    return this.prisma.temperature.deleteMany({
      where: {
        sensor: {
          area: {
            floor: {
              companyId,
            },
          },
        },
      },
    });
  }
  async getDataForMl() {
    return this.prisma.temperature.findMany({
      include: {
        sensor: {
          include: {
            area: {
              include: {
                floor: {
                  include: {
                    company: true,
                  },
                },
              },
            },
          },
        },
      },
    });
  }
  async getTemperatureDataByFloor(query: GetGroupedDataDto, floorId: string) {
    const { startDate, endDate, groupBy } = query;
    const temperature = await this.prisma.temperature.findMany({
      where: {
        sensor: {
          area: {
            floorId,
          },
        },
        createdAt: {
          lte: endDate,
          gte: startDate,
        },
      },
    });
    return groupByDate(temperature, groupBy, 'temp');
  }
  alertSensor() {
    this.alertService.emit('alert', {
      message: 'fire_alert',
    });
  }

  async addTemperatureEntry(
    sensorId: string,
    temperature: number,
    humidity: number,
  ) {
    const room = await this.prisma.sensor.findUnique({
      where: { id: sensorId },
      select: { area: { select: { id: true } } },
    });
    if (!room) {
      throw new Error('Room not found , sensorId: ' + sensorId);
    }
    const areaId = room.area.id;
    const now = new Date();
    const predictionBody = await this.prisma.sensor.findUnique({
      where: { id: sensorId },
      include: { area: { include: { floor: true } } },
    });
    const aiPrediction =
      await this.httpService.axiosRef.post<AiTemperaturePrediction>(
        process.env.PYTHON_BASE_URL + '/temp_prediction',
        {
          id:sensorId,
          sensorId,
          sensor: predictionBody,
          createdAt: now,
          humidity,
        },
      );
    return this.prisma.temperature.create({
      data: {
        temp: temperature,
        humidity,
        aiPrediction: aiPrediction.data.predicted_temperature[0],
        aiHumidityPrediction: aiPrediction.data.humidity??0,
        sensor: {
          connect: {
            id: sensorId,
          },
        },
      },
    });
  }
  async getEntriesByArea(areaId: string, query: GetGroupedDataDto) {
    return this.prisma.temperature.findMany({
      where: {
        sensor: {
          areaId,
        },
        createdAt: {
          lte: query.endDate,
          gte: query.startDate,
        },
      },
      orderBy: {
        createdAt: 'asc',
      },
    });
  }
  async getTemperatureData(query: GetGroupedDataDto, areaId: string) {
    const { startDate, endDate, groupBy } = query;
    const temperature = await this.prisma.temperature.findMany({
      where: {
        sensor: {
          areaId,
        },
        createdAt: {
          lte: endDate,
          gte: startDate,
        },
      },
    });
    const groupedData = groupByDate(temperature, groupBy, 'temp');

    return groupedData;
  }
  async getTempertureEntriesPerFloor(
    floorId: string,
    startDate: Date,
    endDate: Date,
  ) {
    const temperature = await this.prisma.temperature.findMany({
      where: {
        sensor: {
          area: {
            floorId,
          },
        },
        createdAt: {
          lte: endDate,
          gte: startDate,
        },
      },
      orderBy: {
        createdAt: 'asc',
      },
    });

    return temperature;
  }
  async getTemperatureEntriesByLastPeridoFloor(
    floorId: string,
    period: GetConsumptionLastDto,
  ) {
    const startDate = new Date();
    const fallback = new Date();
    switch (period.type) {
      case 'DAY':
        startDate.setDate(startDate.getDate() - 1);
        break;
      case 'WEEK':
        startDate.setDate(startDate.getDate() - 7);
        break;
      case 'MONTH':
        startDate.setMonth(startDate.getMonth() - 1);
        break;
    }
    const temperature = await this.prisma.temperature.findMany({
      where: {
        sensor: {
          area: {
            floorId,
          },
        },
        createdAt: {
          lte: fallback,
          gte: startDate,
        },
      },
      orderBy: {
        createdAt: 'asc',
      },
    });

    return temperature;
  }
  async getTemperatureEntriesByLastPeriodArea(
    areaId: string,
    period: GetConsumptionLastDto,
  ) {
    const startDate = new Date();
    const fallback = new Date();
    switch (period.type) {
      case 'DAY':
        startDate.setDate(startDate.getDate() - 1);
        break;
      case 'WEEK':
        startDate.setDate(startDate.getDate() - 7);
        break;
      case 'MONTH':
        startDate.setMonth(startDate.getMonth() - 1);
        break;
    }
    const temperature = await this.prisma.temperature.findMany({
      where: {
        sensor: {
          areaId,
        },
        createdAt: {
          lte: fallback,
          gte: startDate,
        },
      },
      orderBy: {
        createdAt: 'asc',
      },
    });

    return temperature;
  }
  getAiPredictionOfLast24HoursOfFloor(){
    
  }
}

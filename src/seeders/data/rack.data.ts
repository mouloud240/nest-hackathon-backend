import { Floor } from 'src/utils/types/racks';

export const sampleFloor: Floor = {
  id: 'floor-1',
  name: 'Ground Floor',
  order: 1,
  companyId: 'company-1',
  areas: [
    {
      id: 'area-a',
      name: 'Server Room A',
      floorId: 'floor-1',
      dataCenterId: 'dc-1',
      type: 'server_room',
      polygon: [
        { x: -5, y: 0 },
        { x: -5, y: 5 },
        { x: 0, y: 5 },
        { x: 0, y: 0 },
      ], // Rectangle for Server Room A
      capacity: 5,
      racks: [
        {
          id: 'rack-a1',
          name: 'Rack A1',
          dataCenterId: 'dc-1',
          areaId: 'area-a',
          locationX: -4,
          locationY: 0,
          locationZ: 0,
          lastMaintenance: '2023-12-15',
          sensors: [
            {
              id: 'sensor-a1-temp',
              name: 'Rack A1 Temperature Sensor',
              areaId: 'area-a',
              rackId: 'rack-a1',
              locationX: -4,
              locationY: 0,
              type: 'TEMPERATURE',
              Temperature: [
                {
                  id: 'temp-a1-1',
                  sensorId: 'sensor-a1-temp',
                  temp: 24.5,
                  humidity: 50,
                  createdAt: '2025-04-11T10:00:00Z',
                },
              ],
            },
          ],
          anomalies: [],
        },
        {
          id: 'rack-a2',
          name: 'Rack A2',
          dataCenterId: 'dc-1',
          areaId: 'area-a',
          locationX: -2,
          locationY: 0,
          locationZ: 0,
          lastMaintenance: '2023-11-10',
          sensors: [
            {
              id: 'sensor-a2-temp',
              name: 'Rack A2 Temperature Sensor',
              areaId: 'area-a',
              rackId: 'rack-a2',
              locationX: -2,
              locationY: 0,
              type: 'TEMPERATURE',
              Temperature: [
                {
                  id: 'temp-a2-1',
                  sensorId: 'sensor-a2-temp',
                  temp: 26.8,
                  humidity: 55,
                  createdAt: '2025-04-11T10:00:00Z',
                },
              ],
            },
          ],
          anomalies: [
            {
              id: 'anomaly-a2-1',
              areaId: 'area-a',
              rackId: 'rack-a2',
              title: 'Rack A2 Fan Warning',
              status: 'active',
              reportedAt: '2025-04-11T09:00:00Z',
              resolvedAt: null,
            },
            {
              id: 'anomaly-a2-2',
              areaId: 'area-a',
              rackId: 'rack-a2',
              title: 'Rack A2 Needs Maintenance',
              status: 'active',
              reportedAt: '2025-04-11T09:00:00Z',
              resolvedAt: null,
            },
          ],
        },
        {
          id: 'rack-a4',
          name: 'Rack A4',
          dataCenterId: 'dc-1',
          areaId: 'area-a',
          locationX: 2,
          locationY: 0,
          locationZ: 0,
          lastMaintenance: '2023-10-20',
          sensors: [
            {
              id: 'sensor-a4-temp',
              name: 'Rack A4 Temperature Sensor',
              areaId: 'area-a',
              rackId: 'rack-a4',
              locationX: 2,
              locationY: 0,
              type: 'TEMPERATURE',
              Temperature: [
                {
                  id: 'temp-a4-1',
                  sensorId: 'sensor-a4-temp',
                  temp: 31.2,
                  humidity: 60,
                  createdAt: '2025-04-11T10:00:00Z',
                },
              ],
            },
          ],
          anomalies: [
            {
              id: 'anomaly-a4-1',
              areaId: 'area-a',
              rackId: 'rack-a4',
              title: 'Rack A4 Fan Failure',
              status: 'active',
              reportedAt: '2025-04-11T09:00:00Z',
              resolvedAt: null,
            },
            {
              id: 'anomaly-a4-2',
              areaId: 'area-a',
              rackId: 'rack-a4',
              title: 'Rack A4 Needs Maintenance',
              status: 'active',
              reportedAt: '2025-04-11T09:00:00Z',
              resolvedAt: null,
            },
          ],
        },
      ],
      cameras: [
        {
          id: 'camera-a1',
          name: 'Camera A1',
          floorId: 'floor-1',
          areaId: 'area-a',
          locationX: -3,
          locationY: 4,
        },
      ],
    },
    {
      id: 'area-b',
      name: 'Server Room B',
      floorId: 'floor-1',
      dataCenterId: 'dc-1',
      type: 'server_room',
      polygon: [
        { x: 0, y: 0 },
        { x: 0, y: 5 },
        { x: 5, y: 5 },
        { x: 5, y: 0 },
      ], // Rectangle for Server Room B
      capacity: 5,
      racks: [
        {
          id: 'rack-b1',
          name: 'Rack B1',
          dataCenterId: 'dc-1',
          areaId: 'area-b',
          locationX: -4,
          locationY: 0,
          locationZ: 3,
          lastMaintenance: '2024-01-10',
          sensors: [
            {
              id: 'sensor-b1-temp',
              name: 'Rack B1 Temperature Sensor',
              areaId: 'area-b',
              rackId: 'rack-b1',
              locationX: -4,
              locationY: 3,
              type: 'TEMPERATURE',
              Temperature: [
                {
                  id: 'temp-b1-1',
                  sensorId: 'sensor-b1-temp',
                  temp: 23.7,
                  humidity: 45,
                  createdAt: '2025-04-11T10:00:00Z',
                },
              ],
            },
          ],
          anomalies: [],
        },
        {
          id: 'rack-b2',
          name: 'Rack B2',
          dataCenterId: 'dc-1',
          areaId: 'area-b',
          locationX: -2,
          locationY: 0,
          locationZ: 3,
          lastMaintenance: '2023-11-25',
          sensors: [
            {
              id: 'sensor-b2-temp',
              name: 'Rack B2 Temperature Sensor',
              areaId: 'area-b',
              rackId: 'rack-b2',
              locationX: -2,
              locationY: 3,
              type: 'TEMPERATURE',
              Temperature: [
                {
                  id: 'temp-b2-1',
                  sensorId: 'sensor-b2-temp',
                  temp: 28.9,
                  humidity: 50,
                  createdAt: '2025-04-11T10:00:00Z',
                },
              ],
            },
          ],
          anomalies: [
            {
              id: 'anomaly-b2-1',
              areaId: 'area-b',
              rackId: 'rack-b2',
              title: 'Rack B2 Fan Warning',
              status: 'active',
              reportedAt: '2025-04-11T09:00:00Z',
              resolvedAt: null,
            },
            {
              id: 'anomaly-b2-2',
              areaId: 'area-b',
              rackId: 'rack-b2',
              title: 'Rack B2 Needs Maintenance',
              status: 'active',
              reportedAt: '2025-04-11T09:00:00Z',
              resolvedAt: null,
            },
          ],
        },
      ],
      cameras: [
        {
          id: 'camera-b1',
          name: 'Camera B1',
          floorId: 'floor-1',
          areaId: 'area-b',
          locationX: 3,
          locationY: 4,
        },
      ],
    },
  ],
};

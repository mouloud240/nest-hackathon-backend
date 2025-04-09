__all__: list[str] = []

import cv2
import cv2.typing
import numpy
import sys
import typing as _typing
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


# Enumerations
DNN_BACKEND_DEFAULT: int
DNN_BACKEND_HALIDE: int
DNN_BACKEND_INFERENCE_ENGINE: int
DNN_BACKEND_OPENCV: int
DNN_BACKEND_VKCOM: int
DNN_BACKEND_CUDA: int
DNN_BACKEND_WEBNN: int
DNN_BACKEND_TIMVX: int
DNN_BACKEND_CANN: int
Backend = int
"""One of [DNN_BACKEND_DEFAULT, DNN_BACKEND_HALIDE, DNN_BACKEND_INFERENCE_ENGINE, DNN_BACKEND_OPENCV, DNN_BACKEND_VKCOM, DNN_BACKEND_CUDA, DNN_BACKEND_WEBNN, DNN_BACKEND_TIMVX, DNN_BACKEND_CANN]"""

DNN_TARGET_CPU: int
DNN_TARGET_OPENCL: int
DNN_TARGET_OPENCL_FP16: int
DNN_TARGET_MYRIAD: int
DNN_TARGET_VULKAN: int
DNN_TARGET_FPGA: int
DNN_TARGET_CUDA: int
DNN_TARGET_CUDA_FP16: int
DNN_TARGET_HDDL: int
DNN_TARGET_NPU: int
DNN_TARGET_CPU_FP16: int
Target = int
"""One of [DNN_TARGET_CPU, DNN_TARGET_OPENCL, DNN_TARGET_OPENCL_FP16, DNN_TARGET_MYRIAD, DNN_TARGET_VULKAN, DNN_TARGET_FPGA, DNN_TARGET_CUDA, DNN_TARGET_CUDA_FP16, DNN_TARGET_HDDL, DNN_TARGET_NPU, DNN_TARGET_CPU_FP16]"""

DNN_LAYOUT_UNKNOWN: int
DNN_LAYOUT_ND: int
DNN_LAYOUT_NCHW: int
DNN_LAYOUT_NCDHW: int
DNN_LAYOUT_NHWC: int
DNN_LAYOUT_NDHWC: int
DNN_LAYOUT_PLANAR: int
DataLayout = int
"""One of [DNN_LAYOUT_UNKNOWN, DNN_LAYOUT_ND, DNN_LAYOUT_NCHW, DNN_LAYOUT_NCDHW, DNN_LAYOUT_NHWC, DNN_LAYOUT_NDHWC, DNN_LAYOUT_PLANAR]"""

DNN_PMODE_NULL: int
DNN_PMODE_CROP_CENTER: int
DNN_PMODE_LETTERBOX: int
ImagePaddingMode = int
"""One of [DNN_PMODE_NULL, DNN_PMODE_CROP_CENTER, DNN_PMODE_LETTERBOX]"""

SoftNMSMethod_SOFTNMS_LINEAR: int
SOFT_NMSMETHOD_SOFTNMS_LINEAR: int
SoftNMSMethod_SOFTNMS_GAUSSIAN: int
SOFT_NMSMETHOD_SOFTNMS_GAUSSIAN: int
SoftNMSMethod = int
"""One of [SoftNMSMethod_SOFTNMS_LINEAR, SOFT_NMSMETHOD_SOFTNMS_LINEAR, SoftNMSMethod_SOFTNMS_GAUSSIAN, SOFT_NMSMETHOD_SOFTNMS_GAUSSIAN]"""



# Classes
class DictValue:
    # Functions
    @_typing.overload
    def __init__(self, i: int) -> None: ...
    @_typing.overload
    def __init__(self, p: float) -> None: ...
    @_typing.overload
    def __init__(self, s: str) -> None: ...

    def isInt(self) -> bool: ...

    def isString(self) -> bool: ...

    def isReal(self) -> bool: ...

    def getIntValue(self, idx: int = ...) -> int: ...

    def getRealValue(self, idx: int = ...) -> float: ...

    def getStringValue(self, idx: int = ...) -> str: ...


class Layer(cv2.Algorithm):
    blobs: _typing.Sequence[cv2.typing.MatLike]
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def preferableTarget(self) -> int: ...

    # Functions
    @_typing.overload
    def finalize(self, inputs: _typing.Sequence[cv2.typing.MatLike], outputs: _typing.Sequence[cv2.typing.MatLike] | None = ...) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @_typing.overload
    def finalize(self, inputs: _typing.Sequence[cv2.UMat], outputs: _typing.Sequence[cv2.UMat] | None = ...) -> _typing.Sequence[cv2.UMat]: ...

    def run(self, inputs: _typing.Sequence[cv2.typing.MatLike], internals: _typing.Sequence[cv2.typing.MatLike], outputs: _typing.Sequence[cv2.typing.MatLike] | None = ...) -> tuple[_typing.Sequence[cv2.typing.MatLike], _typing.Sequence[cv2.typing.MatLike]]: ...

    def outputNameToIndex(self, outputName: str) -> int: ...


class Net:
    # Functions
    def __init__(self) -> None: ...

    @classmethod
    @_typing.overload
    def readFromModelOptimizer(cls, xml: str, bin: str) -> Net: ...
    @classmethod
    @_typing.overload
    def readFromModelOptimizer(cls, bufferModelConfig: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]], bufferWeights: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]]) -> Net: ...

    def empty(self) -> bool: ...

    def dump(self) -> str: ...

    def dumpToFile(self, path: str) -> None: ...

    def dumpToPbtxt(self, path: str) -> None: ...

    def addLayer(self, name: str, type: str, dtype: int, params: cv2.typing.LayerParams) -> int: ...

    def addLayerToPrev(self, name: str, type: str, dtype: int, params: cv2.typing.LayerParams) -> int: ...

    def getLayerId(self, layer: str) -> int: ...

    def getLayerNames(self) -> _typing.Sequence[str]: ...

    @_typing.overload
    def getLayer(self, layerId: int) -> Layer: ...
    @_typing.overload
    def getLayer(self, layerName: str) -> Layer: ...
    @_typing.overload
    def getLayer(self, layerId: cv2.typing.LayerId) -> Layer: ...

    def connect(self, outPin: str, inpPin: str) -> None: ...

    def setInputsNames(self, inputBlobNames: _typing.Sequence[str]) -> None: ...

    def setInputShape(self, inputName: str, shape: cv2.typing.MatShape) -> None: ...

    @_typing.overload
    def forward(self, outputName: str = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def forward(self, outputBlobs: _typing.Sequence[cv2.typing.MatLike] | None = ..., outputName: str = ...) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @_typing.overload
    def forward(self, outputBlobs: _typing.Sequence[cv2.UMat] | None = ..., outputName: str = ...) -> _typing.Sequence[cv2.UMat]: ...
    @_typing.overload
    def forward(self, outBlobNames: _typing.Sequence[str], outputBlobs: _typing.Sequence[cv2.typing.MatLike] | None = ...) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @_typing.overload
    def forward(self, outBlobNames: _typing.Sequence[str], outputBlobs: _typing.Sequence[cv2.UMat] | None = ...) -> _typing.Sequence[cv2.UMat]: ...

    def forwardAsync(self, outputName: str = ...) -> cv2.AsyncArray: ...

    def forwardAndRetrieve(self, outBlobNames: _typing.Sequence[str]) -> _typing.Sequence[_typing.Sequence[cv2.typing.MatLike]]: ...

    @_typing.overload
    def quantize(self, calibData: _typing.Sequence[cv2.typing.MatLike], inputsDtype: int, outputsDtype: int, perChannel: bool = ...) -> Net: ...
    @_typing.overload
    def quantize(self, calibData: _typing.Sequence[cv2.UMat], inputsDtype: int, outputsDtype: int, perChannel: bool = ...) -> Net: ...

    def getInputDetails(self) -> tuple[_typing.Sequence[float], _typing.Sequence[int]]: ...

    def getOutputDetails(self) -> tuple[_typing.Sequence[float], _typing.Sequence[int]]: ...

    def setHalideScheduler(self, scheduler: str) -> None: ...

    def setPreferableBackend(self, backendId: int) -> None: ...

    def setPreferableTarget(self, targetId: int) -> None: ...

    @_typing.overload
    def setInput(self, blob: cv2.typing.MatLike, name: str = ..., scalefactor: float = ..., mean: cv2.typing.Scalar = ...) -> None: ...
    @_typing.overload
    def setInput(self, blob: cv2.UMat, name: str = ..., scalefactor: float = ..., mean: cv2.typing.Scalar = ...) -> None: ...

    @_typing.overload
    def setParam(self, layer: int, numParam: int, blob: cv2.typing.MatLike) -> None: ...
    @_typing.overload
    def setParam(self, layerName: str, numParam: int, blob: cv2.typing.MatLike) -> None: ...

    @_typing.overload
    def getParam(self, layer: int, numParam: int = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def getParam(self, layerName: str, numParam: int = ...) -> cv2.typing.MatLike: ...

    def getUnconnectedOutLayers(self) -> _typing.Sequence[int]: ...

    def getUnconnectedOutLayersNames(self) -> _typing.Sequence[str]: ...

    @_typing.overload
    def getLayersShapes(self, netInputShapes: _typing.Sequence[cv2.typing.MatShape]) -> tuple[_typing.Sequence[int], _typing.Sequence[_typing.Sequence[cv2.typing.MatShape]], _typing.Sequence[_typing.Sequence[cv2.typing.MatShape]]]: ...
    @_typing.overload
    def getLayersShapes(self, netInputShape: cv2.typing.MatShape) -> tuple[_typing.Sequence[int], _typing.Sequence[_typing.Sequence[cv2.typing.MatShape]], _typing.Sequence[_typing.Sequence[cv2.typing.MatShape]]]: ...

    @_typing.overload
    def getFLOPS(self, netInputShapes: _typing.Sequence[cv2.typing.MatShape]) -> int: ...
    @_typing.overload
    def getFLOPS(self, netInputShape: cv2.typing.MatShape) -> int: ...
    @_typing.overload
    def getFLOPS(self, layerId: int, netInputShapes: _typing.Sequence[cv2.typing.MatShape]) -> int: ...
    @_typing.overload
    def getFLOPS(self, layerId: int, netInputShape: cv2.typing.MatShape) -> int: ...

    def getLayerTypes(self) -> _typing.Sequence[str]: ...

    def getLayersCount(self, layerType: str) -> int: ...

    @_typing.overload
    def getMemoryConsumption(self, netInputShape: cv2.typing.MatShape) -> tuple[int, int]: ...
    @_typing.overload
    def getMemoryConsumption(self, layerId: int, netInputShapes: _typing.Sequence[cv2.typing.MatShape]) -> tuple[int, int]: ...
    @_typing.overload
    def getMemoryConsumption(self, layerId: int, netInputShape: cv2.typing.MatShape) -> tuple[int, int]: ...

    def enableFusion(self, fusion: bool) -> None: ...

    def enableWinograd(self, useWinograd: bool) -> None: ...

    def getPerfProfile(self) -> tuple[int, _typing.Sequence[float]]: ...


class Image2BlobParams:
    scalefactor: cv2.typing.Scalar
    size: cv2.typing.Size
    mean: cv2.typing.Scalar
    swapRB: bool
    ddepth: int
    datalayout: DataLayout
    paddingmode: ImagePaddingMode
    borderValue: cv2.typing.Scalar

    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, scalefactor: cv2.typing.Scalar, size: cv2.typing.Size = ..., mean: cv2.typing.Scalar = ..., swapRB: bool = ..., ddepth: int = ..., datalayout: DataLayout = ..., mode: ImagePaddingMode = ..., borderValue: cv2.typing.Scalar = ...) -> None: ...

    def blobRectToImageRect(self, rBlob: cv2.typing.Rect, size: cv2.typing.Size) -> cv2.typing.Rect: ...

    def blobRectsToImageRects(self, rBlob: _typing.Sequence[cv2.typing.Rect], size: cv2.typing.Size) -> _typing.Sequence[cv2.typing.Rect]: ...


class Model:
    # Functions
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...
    @_typing.overload
    def __init__(self, network: Net) -> None: ...

    @_typing.overload
    def setInputSize(self, size: cv2.typing.Size) -> Model: ...
    @_typing.overload
    def setInputSize(self, width: int, height: int) -> Model: ...

    def setInputMean(self, mean: cv2.typing.Scalar) -> Model: ...

    def setInputScale(self, scale: cv2.typing.Scalar) -> Model: ...

    def setInputCrop(self, crop: bool) -> Model: ...

    def setInputSwapRB(self, swapRB: bool) -> Model: ...

    def setOutputNames(self, outNames: _typing.Sequence[str]) -> Model: ...

    def setInputParams(self, scale: float = ..., size: cv2.typing.Size = ..., mean: cv2.typing.Scalar = ..., swapRB: bool = ..., crop: bool = ...) -> None: ...

    @_typing.overload
    def predict(self, frame: cv2.typing.MatLike, outs: _typing.Sequence[cv2.typing.MatLike] | None = ...) -> _typing.Sequence[cv2.typing.MatLike]: ...
    @_typing.overload
    def predict(self, frame: cv2.UMat, outs: _typing.Sequence[cv2.UMat] | None = ...) -> _typing.Sequence[cv2.UMat]: ...

    def setPreferableBackend(self, backendId: Backend) -> Model: ...

    def setPreferableTarget(self, targetId: Target) -> Model: ...

    def enableWinograd(self, useWinograd: bool) -> Model: ...


class ClassificationModel(Model):
    # Functions
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...
    @_typing.overload
    def __init__(self, network: Net) -> None: ...

    def setEnableSoftmaxPostProcessing(self, enable: bool) -> ClassificationModel: ...

    def getEnableSoftmaxPostProcessing(self) -> bool: ...

    @_typing.overload
    def classify(self, frame: cv2.typing.MatLike) -> tuple[int, float]: ...
    @_typing.overload
    def classify(self, frame: cv2.UMat) -> tuple[int, float]: ...


class KeypointsModel(Model):
    # Functions
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...
    @_typing.overload
    def __init__(self, network: Net) -> None: ...

    @_typing.overload
    def estimate(self, frame: cv2.typing.MatLike, thresh: float = ...) -> _typing.Sequence[cv2.typing.Point2f]: ...
    @_typing.overload
    def estimate(self, frame: cv2.UMat, thresh: float = ...) -> _typing.Sequence[cv2.typing.Point2f]: ...


class SegmentationModel(Model):
    # Functions
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...
    @_typing.overload
    def __init__(self, network: Net) -> None: ...

    @_typing.overload
    def segment(self, frame: cv2.typing.MatLike, mask: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def segment(self, frame: cv2.UMat, mask: cv2.UMat | None = ...) -> cv2.UMat: ...


class DetectionModel(Model):
    # Functions
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...
    @_typing.overload
    def __init__(self, network: Net) -> None: ...

    def setNmsAcrossClasses(self, value: bool) -> DetectionModel: ...

    def getNmsAcrossClasses(self) -> bool: ...

    @_typing.overload
    def detect(self, frame: cv2.typing.MatLike, confThreshold: float = ..., nmsThreshold: float = ...) -> tuple[_typing.Sequence[int], _typing.Sequence[float], _typing.Sequence[cv2.typing.Rect]]: ...
    @_typing.overload
    def detect(self, frame: cv2.UMat, confThreshold: float = ..., nmsThreshold: float = ...) -> tuple[_typing.Sequence[int], _typing.Sequence[float], _typing.Sequence[cv2.typing.Rect]]: ...


class TextRecognitionModel(Model):
    # Functions
    @_typing.overload
    def __init__(self, network: Net) -> None: ...
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...

    def setDecodeType(self, decodeType: str) -> TextRecognitionModel: ...

    def getDecodeType(self) -> str: ...

    def setDecodeOptsCTCPrefixBeamSearch(self, beamSize: int, vocPruneSize: int = ...) -> TextRecognitionModel: ...

    def setVocabulary(self, vocabulary: _typing.Sequence[str]) -> TextRecognitionModel: ...

    def getVocabulary(self) -> _typing.Sequence[str]: ...

    @_typing.overload
    def recognize(self, frame: cv2.typing.MatLike) -> str: ...
    @_typing.overload
    def recognize(self, frame: cv2.UMat) -> str: ...
    @_typing.overload
    def recognize(self, frame: cv2.typing.MatLike, roiRects: _typing.Sequence[cv2.typing.MatLike]) -> _typing.Sequence[str]: ...
    @_typing.overload
    def recognize(self, frame: cv2.UMat, roiRects: _typing.Sequence[cv2.UMat]) -> _typing.Sequence[str]: ...


class TextDetectionModel(Model):
    # Functions
    @_typing.overload
    def detect(self, frame: cv2.typing.MatLike) -> tuple[_typing.Sequence[_typing.Sequence[cv2.typing.Point]], _typing.Sequence[float]]: ...
    @_typing.overload
    def detect(self, frame: cv2.UMat) -> tuple[_typing.Sequence[_typing.Sequence[cv2.typing.Point]], _typing.Sequence[float]]: ...
    @_typing.overload
    def detect(self, frame: cv2.typing.MatLike) -> _typing.Sequence[_typing.Sequence[cv2.typing.Point]]: ...
    @_typing.overload
    def detect(self, frame: cv2.UMat) -> _typing.Sequence[_typing.Sequence[cv2.typing.Point]]: ...

    @_typing.overload
    def detectTextRectangles(self, frame: cv2.typing.MatLike) -> tuple[_typing.Sequence[cv2.typing.RotatedRect], _typing.Sequence[float]]: ...
    @_typing.overload
    def detectTextRectangles(self, frame: cv2.UMat) -> tuple[_typing.Sequence[cv2.typing.RotatedRect], _typing.Sequence[float]]: ...
    @_typing.overload
    def detectTextRectangles(self, frame: cv2.typing.MatLike) -> _typing.Sequence[cv2.typing.RotatedRect]: ...
    @_typing.overload
    def detectTextRectangles(self, frame: cv2.UMat) -> _typing.Sequence[cv2.typing.RotatedRect]: ...


class TextDetectionModel_EAST(TextDetectionModel):
    # Functions
    @_typing.overload
    def __init__(self, network: Net) -> None: ...
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...

    def setConfidenceThreshold(self, confThreshold: float) -> TextDetectionModel_EAST: ...

    def getConfidenceThreshold(self) -> float: ...

    def setNMSThreshold(self, nmsThreshold: float) -> TextDetectionModel_EAST: ...

    def getNMSThreshold(self) -> float: ...


class TextDetectionModel_DB(TextDetectionModel):
    # Functions
    @_typing.overload
    def __init__(self, network: Net) -> None: ...
    @_typing.overload
    def __init__(self, model: str, config: str = ...) -> None: ...

    def setBinaryThreshold(self, binaryThreshold: float) -> TextDetectionModel_DB: ...

    def getBinaryThreshold(self) -> float: ...

    def setPolygonThreshold(self, polygonThreshold: float) -> TextDetectionModel_DB: ...

    def getPolygonThreshold(self) -> float: ...

    def setUnclipRatio(self, unclipRatio: float) -> TextDetectionModel_DB: ...

    def getUnclipRatio(self) -> float: ...

    def setMaxCandidates(self, maxCandidates: int) -> TextDetectionModel_DB: ...

    def getMaxCandidates(self) -> int: ...


class LayerProtocol(Protocol):
    # Functions
    def __init__(self, params: dict[str, DictValue], blobs: _typing.Sequence[cv2.typing.MatLike]) -> None: ...

    def getMemoryShapes(self, inputs: _typing.Sequence[_typing.Sequence[int]]) -> _typing.Sequence[_typing.Sequence[int]]: ...

    def forward(self, inputs: _typing.Sequence[cv2.typing.MatLike]) -> _typing.Sequence[cv2.typing.MatLike]: ...



# Functions
def NMSBoxes(bboxes: _typing.Sequence[cv2.typing.Rect2d], scores: _typing.Sequence[float], score_threshold: float, nms_threshold: float, eta: float = ..., top_k: int = ...) -> _typing.Sequence[int]: ...

def NMSBoxesBatched(bboxes: _typing.Sequence[cv2.typing.Rect2d], scores: _typing.Sequence[float], class_ids: _typing.Sequence[int], score_threshold: float, nms_threshold: float, eta: float = ..., top_k: int = ...) -> _typing.Sequence[int]: ...

def NMSBoxesRotated(bboxes: _typing.Sequence[cv2.typing.RotatedRect], scores: _typing.Sequence[float], score_threshold: float, nms_threshold: float, eta: float = ..., top_k: int = ...) -> _typing.Sequence[int]: ...

@_typing.overload
def blobFromImage(image: cv2.typing.MatLike, scalefactor: float = ..., size: cv2.typing.Size = ..., mean: cv2.typing.Scalar = ..., swapRB: bool = ..., crop: bool = ..., ddepth: int = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImage(image: cv2.UMat, scalefactor: float = ..., size: cv2.typing.Size = ..., mean: cv2.typing.Scalar = ..., swapRB: bool = ..., crop: bool = ..., ddepth: int = ...) -> cv2.typing.MatLike: ...

@_typing.overload
def blobFromImageWithParams(image: cv2.typing.MatLike, param: Image2BlobParams = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImageWithParams(image: cv2.UMat, param: Image2BlobParams = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImageWithParams(image: cv2.typing.MatLike, blob: cv2.typing.MatLike | None = ..., param: Image2BlobParams = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImageWithParams(image: cv2.UMat, blob: cv2.UMat | None = ..., param: Image2BlobParams = ...) -> cv2.UMat: ...

@_typing.overload
def blobFromImages(images: _typing.Sequence[cv2.typing.MatLike], scalefactor: float = ..., size: cv2.typing.Size = ..., mean: cv2.typing.Scalar = ..., swapRB: bool = ..., crop: bool = ..., ddepth: int = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImages(images: _typing.Sequence[cv2.UMat], scalefactor: float = ..., size: cv2.typing.Size = ..., mean: cv2.typing.Scalar = ..., swapRB: bool = ..., crop: bool = ..., ddepth: int = ...) -> cv2.typing.MatLike: ...

@_typing.overload
def blobFromImagesWithParams(images: _typing.Sequence[cv2.typing.MatLike], param: Image2BlobParams = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImagesWithParams(images: _typing.Sequence[cv2.UMat], param: Image2BlobParams = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImagesWithParams(images: _typing.Sequence[cv2.typing.MatLike], blob: cv2.typing.MatLike | None = ..., param: Image2BlobParams = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def blobFromImagesWithParams(images: _typing.Sequence[cv2.UMat], blob: cv2.UMat | None = ..., param: Image2BlobParams = ...) -> cv2.UMat: ...

def getAvailableTargets(be: Backend) -> _typing.Sequence[Target]: ...

@_typing.overload
def imagesFromBlob(blob_: cv2.typing.MatLike, images_: _typing.Sequence[cv2.typing.MatLike] | None = ...) -> _typing.Sequence[cv2.typing.MatLike]: ...
@_typing.overload
def imagesFromBlob(blob_: cv2.typing.MatLike, images_: _typing.Sequence[cv2.UMat] | None = ...) -> _typing.Sequence[cv2.UMat]: ...

@_typing.overload
def readNet(model: str, config: str = ..., framework: str = ...) -> Net: ...
@_typing.overload
def readNet(framework: str, bufferModel: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]], bufferConfig: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]] = ...) -> Net: ...

@_typing.overload
def readNetFromCaffe(prototxt: str, caffeModel: str = ...) -> Net: ...
@_typing.overload
def readNetFromCaffe(bufferProto: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]], bufferModel: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]] = ...) -> Net: ...

@_typing.overload
def readNetFromDarknet(cfgFile: str, darknetModel: str = ...) -> Net: ...
@_typing.overload
def readNetFromDarknet(bufferCfg: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]], bufferModel: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]] = ...) -> Net: ...

@_typing.overload
def readNetFromModelOptimizer(xml: str, bin: str = ...) -> Net: ...
@_typing.overload
def readNetFromModelOptimizer(bufferModelConfig: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]], bufferWeights: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]]) -> Net: ...

@_typing.overload
def readNetFromONNX(onnxFile: str) -> Net: ...
@_typing.overload
def readNetFromONNX(buffer: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]]) -> Net: ...

@_typing.overload
def readNetFromTFLite(model: str) -> Net: ...
@_typing.overload
def readNetFromTFLite(bufferModel: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]]) -> Net: ...

@_typing.overload
def readNetFromTensorflow(model: str, config: str = ...) -> Net: ...
@_typing.overload
def readNetFromTensorflow(bufferModel: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]], bufferConfig: numpy.ndarray[_typing.Any, numpy.dtype[numpy.uint8]] = ...) -> Net: ...

def readNetFromTorch(model: str, isBinary: bool = ..., evaluate: bool = ...) -> Net: ...

def readTensorFromONNX(path: str) -> cv2.typing.MatLike: ...

def readTorchBlob(filename: str, isBinary: bool = ...) -> cv2.typing.MatLike: ...

def shrinkCaffeModel(src: str, dst: str, layersTypes: _typing.Sequence[str] = ...) -> None: ...

def softNMSBoxes(bboxes: _typing.Sequence[cv2.typing.Rect], scores: _typing.Sequence[float], score_threshold: float, nms_threshold: float, top_k: int = ..., sigma: float = ..., method: SoftNMSMethod = ...) -> tuple[_typing.Sequence[float], _typing.Sequence[int]]: ...

def writeTextGraph(model: str, output: str) -> None: ...



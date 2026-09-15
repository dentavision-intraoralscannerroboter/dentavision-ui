from __future__ import annotations

import platform

import cv2


def _default_backend() -> int:
    system = platform.system()
    if system == "Darwin":
        return cv2.CAP_AVFOUNDATION
    if system == "Windows":
        return cv2.CAP_DSHOW
    return cv2.CAP_V4L2  # Linux


class Camera:
    def __init__(self, index: int = 0, backend: int | None = None):
        self.capture = cv2.VideoCapture(index, backend or _default_backend())
        if not self.capture.isOpened():
            raise RuntimeError("Failed to open camera. Check camera permissions and availability.")

    def read_frame(self):
        success, frame = self.capture.read()
        if not success:
            return None
        return frame

    def release(self):
        self.capture.release()

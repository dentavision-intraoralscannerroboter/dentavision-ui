from PySide6.QtGui import QImage, QPixmap


def to_pixmap(rgb_frame, w: int, h: int, ch: int) -> QPixmap:
    image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
    return QPixmap.fromImage(image)
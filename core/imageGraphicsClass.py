# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''item/view 架构'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core.模板匹配.STMOperateDb import STMOperateDb
from lib.image import *

from lib.path import globalsdynamic, Globals, path_join
from lib.utils import setLabelCentral, KeepAspectScale


class SelectionBox(QGraphicsItem):

    def __init__(
            self,
            id="SELECTION_BOX_1",
            pos=QPointF(0, 0),
            size=QSizeF(100, 50),
            minSize=QSizeF(30, 30),
            limitRect=QRectF(0, 0, 500, 500),
            centerPen=QPen(Qt.gray, 2),
            centerBrush=QBrush(QColor(10, 10, 10, 100)),
            cornerPen=QPen(Qt.black, 2),
            cornerSize=QSizeF(10, 10),
            cornerBrush=QBrush(Qt.white),
            type='矩形',
            sort='选取框',
    ):
        '''

        :param id: id
        :param pos: 左上角点的坐标，要加上self.playbackItem.pos()
        :param size: 尺寸
        :param minSize: 最小尺寸
        :param limitRect:
        :param centerPen: 边框
        :param centerBrush: 中心颜色
        :param cornerPen: 四角点
        :param cornerSize: 角的大小
        :param cornerBrush: 角的颜色
        # :param IsUse: 是否可以使用
        :param type: 绘制类型
        :param sort: 分类
        '''
        super().__init__()

        self.id = id
        self.size = size
        self.initSize = size  # 初始大小
        self.innerSize = size / 2
        self.centerPen = centerPen
        self.centerBrush = centerBrush
        self.cornerPen = cornerPen
        self.cornerSize = cornerSize
        self.cornerFix = None
        self.refreshCornerFix()
        self.cornerBrush = cornerBrush
        self.type = type
        self.sort = sort

        self.dragFlag = None
        self.ItemVisible = True  # 图形是否绘制
        self.dragDiff = None
        self.minSize = minSize
        self.limitRect = limitRect

        self.setPos(pos)
        self.setAcceptHoverEvents(True)

        # four corner rect in item

    def set_active(self, flag=True):
        '''设置激活的item'''
        if flag:
            # self.id = "activeBox"
            self.cornerPen = QPen(Qt.red, 2)
            self.setEnabled(True)

            for other_item in self.scene().items():
                if other_item != self:
                    # other_item.id = "SelectionBox"
                    other_item.cornerPen = QPen(Qt.black, 2)
                    other_item.setEnabled(False)
        else:
            # self.id = "SelectionBox"
            self.cornerPen = QPen(Qt.black, 2)
            self.setEnabled(True)

            for other_item in self.scene().items():
                if other_item != self:
                    # other_item.id = "activeBox"
                    other_item.cornerPen = QPen(Qt.red, 2)
                    other_item.setEnabled(False)

    def setRoundSize(self, size):
        if size.width() > size.height():
            size = QSizeF(size.height(), size.height())
        else:
            size = QSizeF(size.width(), size.width())
        return size

    def centerRect(self):
        '''图形约束条件'''
        if self.type == '圆形':
            self.size = self.setRoundSize(self.size)
        elif self.type == '圆环':
            self.size = self.setRoundSize(self.size)
            self.innerSize = self.setRoundSize(self.innerSize)

            # 限制内圆尺寸
            if self.innerSize.width() > self.size.width() - 30:
                self.innerSize = QSizeF(self.size.width() - 30, self.size.height() - 30)
            w, h = self.innerSize.width(), self.innerSize.height()
            minSizeW = self.minSize.width() - 30 if self.minSize.width() - 30 >= 30 else 30
            minSizeH = self.minSize.height() - 30 if self.minSize.height() - 30 >= 30 else 30
            if self.innerSize.width() < minSizeW:
                w = minSizeW
            if self.innerSize.height() < minSizeH:
                h = minSizeH
            self.innerSize = self.setRoundSize(QSizeF(w, h))
        return QRectF(QPointF(0, 0), self.size)

    # 动作节点左上角坐标
    def rotateCornerRect(self, ):
        topLeft = QRectF(self.itemTopLeft() - self.cornerFix, self.cornerSize)
        topLeft = QRectF(QPoint(topLeft.x() + self.size.width() / 2, topLeft.y() + self.m_rLen), topLeft.size())
        return topLeft

    def topLeftCornerRect(self):
        topLeft = QRectF(self.itemTopLeft() - self.cornerFix, self.cornerSize)
        topLeft = QRectF(QPoint(topLeft.x() + self.size.width() / 2, topLeft.y()), topLeft.size())
        return topLeft

    def topRightCornerRect(self):
        topRight = QRectF(self.itemTopRight() - self.cornerFix, self.cornerSize)
        topRight = QRectF(QPoint(topRight.x(), topRight.y() + self.size.height() / 2), topRight.size())
        return topRight

    def bottomLeftCornerRect(self):
        bottomLeft = QRectF(self.itemBottomLeft() - self.cornerFix, self.cornerSize)
        bottomLeft = QRectF(QPoint(bottomLeft.x(), bottomLeft.y() - self.size.height() / 2), bottomLeft.size())
        return bottomLeft

    def bottomRightCornerRect(self):
        bottomRight = QRectF(self.itemBottomRight() - self.cornerFix, self.cornerSize)
        bottomRight = QRectF(QPoint(bottomRight.x() - self.size.width() / 2, bottomRight.y()), bottomRight.size())
        return bottomRight

    def innerTopLeftCornerRect(self):
        topLeft = QRectF(self.innerItemTopLeft() - self.cornerFix, self.cornerSize)
        topLeft = QRectF(QPoint(topLeft.x() + self.innerSize.width() / 2, topLeft.y()), topLeft.size())
        return topLeft

    def innerTopRightCornerRect(self):
        topRight = QRectF(self.innerItemTopRight() - self.cornerFix, self.cornerSize)
        topRight = QRectF(QPoint(topRight.x(), topRight.y() + self.innerSize.height() / 2), topRight.size())
        return topRight

    def innerBottomLeftCornerRect(self):
        bottomLeft = QRectF(self.innerItemBottomLeft() - self.cornerFix, self.cornerSize)
        bottomLeft = QRectF(QPoint(bottomLeft.x(), bottomLeft.y() - self.innerSize.height() / 2), bottomLeft.size())
        return bottomLeft

    def innerBottomRightCornerRect(self):
        bottomRight = QRectF(self.innerItemBottomRight() - self.cornerFix, self.cornerSize)
        bottomRight = QRectF(QPoint(bottomRight.x() - self.innerSize.width() / 2, bottomRight.y()), bottomRight.size())
        return bottomRight

    # 图形顶点坐标
    def itemTopLeft(self):
        return QPointF(0, 0)
        # return QPointF(self.size.width() / 2, 0)

    def itemTopRight(self):
        return QPointF(self.size.width(), 0)
        # return QPointF(self.size.width(), self.size.height() / 2)

    def itemBottomLeft(self):
        return QPointF(0, self.size.height())
        # return QPointF(0, self.size.height() - self.size.height() / 2)

    def itemBottomRight(self):
        return QPointF(self.size.width(), self.size.height())
        # return QPointF(self.size.width() - self.size.width() / 2, self.size.height())

    def innerItemTopLeft(self):
        return QPointF((self.size.width() - self.innerSize.width()) / 2,
                       (self.size.height() - self.innerSize.height()) / 2)

    def innerItemTopRight(self):
        return QPointF((self.size.width() + self.innerSize.width()) / 2,
                       (self.size.height() - self.innerSize.height()) / 2)

    def innerItemBottomLeft(self):
        return QPointF((self.size.width() - self.innerSize.width()) / 2,
                       (self.size.height() + self.innerSize.height()) / 2)

    def innerItemBottomRight(self):
        return QPointF((self.size.width() + self.innerSize.width()) / 2,
                       (self.size.height() + self.innerSize.height()) / 2)

    # 场景中的四个角点位置
    def sceneTopLeft(self):
        return self.mapToScene(self.itemTopLeft())

    def sceneTopRight(self):
        return self.mapToScene(self.itemTopRight())

    def sceneBottomLeft(self):
        return self.mapToScene(self.itemBottomLeft())

    def sceneBottomRight(self):
        return self.mapToScene(self.itemBottomRight())

    def innerSceneTopLeft(self):
        return self.mapToScene(self.innerItemTopLeft())

    def innerSceneTopRight(self):
        return self.mapToScene(self.innerItemTopRight())

    def innerSceneBottomLeft(self):
        return self.mapToScene(self.innerItemBottomLeft())

    def innerSceneBottomRight(self):
        return self.mapToScene(self.innerItemBottomRight())

    def refreshCornerFix(self):
        self.cornerFix = QPointF(self.cornerSize.width() / 2, self.cornerSize.height() / 2)

    def boundingRect(self):
        # 调整边界矩形的大小
        return QRectF(-self.cornerFix, self.size + self.cornerSize)

    def paint(self, painter, option, widget):
        '''绘制框'''
        try:
            if self.ItemVisible:
                if self.type == '标定':
                    if self.isEnabled():
                        pixmap = QPixmap(path_join(Globals.project_path, "icon/目标-02-红.png"))
                    else:
                        pixmap = QPixmap(path_join(Globals.project_path, "icon/目标-02-蓝.png"))
                    # 调整图像大小
                    # self.scene().addPixmap(pixmap)
                    painter.drawPixmap(
                        QRectF(QPoint(0, 0), QSizeF(self.initSize.width(), self.initSize.height())).toRect(), pixmap)
                    # 是否绘制定点
                    self.cornerSize = QSizeF(0, 0)
                    # self.refreshCornerFix()
                    return None

                cornerXRadius = self.cornerFix.x()  # 获取圆角椭圆的X轴半径
                cornerYRadius = self.cornerFix.y()  # 获取圆角椭圆的Y轴半径
                if self.type == '矩形':
                    painter.setPen(self.centerPen)  # 设置绘制笔的属性，包括颜色、线宽等
                    painter.setBrush(self.centerBrush)  # 设置填充笔的属性，包括颜色、填充样式等
                    painter.drawRect(self.centerRect())  # 绘制一个矩形框

                elif self.type == '圆形':
                    painter.setPen(self.centerPen)  # 设置绘制笔的属性，包括颜色、线宽等
                    painter.setBrush(self.centerBrush)  # 设置填充笔的属性，包括颜色、填充样式等
                    painter.drawEllipse(self.centerRect())  # 绘制一个圆形框
                elif self.type == '圆环':
                    # painter.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿
                    painter.setPen(self.centerPen)  # 设置绘制笔的属性，包括颜色、线宽等
                    painter.setBrush(self.centerBrush)  # 设置填充笔的属性，包括颜色、填充样式等
                    self.outerRect = self.centerRect()
                    self.innerRect = QRectF(self.innerItemTopLeft(), self.innerSize)
                    painter.drawEllipse(self.innerRect)  # 绘制内圆
                    painter.drawEllipse(self.outerRect)  # 绘制外圆

                    # 绘制内圆节点
                    painter.setPen(self.cornerPen)
                    painter.setBrush(self.cornerBrush)
                    painter.drawRoundedRect(self.innerTopLeftCornerRect(), cornerXRadius,
                                            cornerYRadius)  # top left  # 绘制一个带有圆角的矩形框
                    painter.drawRoundedRect(self.innerTopRightCornerRect(), cornerXRadius, cornerYRadius)  # top right
                    painter.drawRoundedRect(self.innerBottomLeftCornerRect(), cornerXRadius,
                                            cornerYRadius)  # bottom left
                    painter.drawRoundedRect(self.innerBottomRightCornerRect(), cornerXRadius, cornerYRadius)
                # 绘制节点
                painter.setPen(self.cornerPen)
                painter.setBrush(self.cornerBrush)
                painter.drawRoundedRect(self.topLeftCornerRect(), cornerXRadius,
                                        cornerYRadius)  # top left  # 绘制一个带有圆角的矩形框
                painter.drawRoundedRect(self.topRightCornerRect(), cornerXRadius, cornerYRadius)  # top right
                painter.drawRoundedRect(self.bottomLeftCornerRect(), cornerXRadius, cornerYRadius)  # bottom left
                painter.drawRoundedRect(self.bottomRightCornerRect(), cornerXRadius, cornerYRadius)
                #  旋转
                # 绘制旋转节点
                # if self.type == '矩形':
                #     painter.setPen(QPen(Qt.black, 1, Qt.DashLine))
                #     painter.setBrush(QBrush(Qt.yellow))
                #     rect = self.centerRect()
                #     m_dLineLen = 20
                #     self.m_rLen = m_dLineLen+cornerXRadius+2
                #     painter.drawLine(rect.center().x(), rect.top() + m_dLineLen, rect.center().x(), rect.top()+cornerXRadius+2)
                #     # 绘制圆
                #     painter.drawRoundedRect(self.rotateCornerRect(), cornerXRadius, cornerYRadius)
        except Exception as e:
            print(e)

    def hoverMoveEvent(self, event):
        '''鼠标悬停事件'''
        # 检查鼠标的位置是否在左上角矩形或右下角矩形内。如果是，则将鼠标光标设置为Qt.SizeFDiagCursor（斜线缩放光标）
        if self.type != '标定':
            if self.topLeftCornerRect().contains(event.pos()) or self.bottomRightCornerRect().contains(event.pos()):
                self.setCursor(Qt.SizeFDiagCursor)
                return
            # 检查鼠标的位置是否在右上角矩形或左下角矩形内。如果是，则将鼠标光标设置为Qt.SizeBDiagCursor（反斜线缩放光标）
            if self.topRightCornerRect().contains(event.pos()) or self.bottomLeftCornerRect().contains(event.pos()):
                self.setCursor(Qt.SizeBDiagCursor)
                return
        if self.type == '圆环':
            # 检查鼠标的位置是否在内圆左上角矩形或右下角矩形内。如果是，则将鼠标光标设置为Qt.SizeFDiagCursor（斜线缩放光标）
            if self.innerTopLeftCornerRect().contains(event.pos()) or self.innerBottomRightCornerRect().contains(
                    event.pos()):
                self.setCursor(Qt.SizeFDiagCursor)
                return
            # 检查鼠标的位置是否在内圆右上角矩形或左下角矩形内。如果是，则将鼠标光标设置为Qt.SizeBDiagCursor（反斜线缩放光标）
            if self.innerTopRightCornerRect().contains(event.pos()) or self.innerBottomLeftCornerRect().contains(
                    event.pos()):
                self.setCursor(Qt.SizeBDiagCursor)
                return
        #  旋转
        # if self.type == '矩形':
        #     # 检查鼠标的位置是否旋转节点内。如果是，则将鼠标光标设置为Qt.SizeBDiagCursor（旋转光标）
        #     if self.rotateCornerRect().contains(event.pos()) :
        #         # 通过QPixmap加载一个图像文件
        #         pixmap = QPixmap(path_join(Globals.project_path,"icon/旋转.png"))
        #         # 调整图像大小
        #         pixmap = pixmap.scaled(20, 20)  # 设置光标大小为32x32像素
        #         # 使用QCursor和QPixmap设置自定义光标形状
        #         cursor = QCursor(pixmap)
        #         self.setCursor(cursor)
        #         return
        # 检查鼠标的位置是否在中心矩形内。如果是，则将鼠标光标设置为Qt.SizeAllCursor（移动光标）
        if self.centerRect().contains(event.pos()):
            self.setCursor(Qt.SizeAllCursor)
            return
        # 鼠标不在任何感兴趣的区域内,将鼠标光标设置为Qt.ArrowCursor（默认光标，箭头光标）
        self.setCursor(Qt.ArrowCursor)

    def contextMenuEvent(self, event):
        '''鼠标右键事件'''
        menu = QMenu()
        delete_action = menu.addAction("删除")
        action = menu.exec_(event.screenPos())

        if action == delete_action:
            self.set_active(False)
            # self.id = "SelectionBox"
            self.setVisible(False)  # 设置项的可见性为False
            scene = self.scene()
            if scene is not None:
                self.prepareGeometryChange()
                scene.removeItem(self)  # 从场景中删除项 没有设置scene.setItemIndexMethod(QGraphicsScene.NoIndex)会闪退

        # 删除掩码更新数据库
        if self.sort == '掩码':
            # mask = {'mask': None}
            # STMOperateDb.add_data(mask)
            data = {}
            data['name'] = globalsdynamic.child
            data['mask'] = None
            globalsdynamic.db_main.insert_data('ImageCapture', data)

    def mousePressEvent(self, event) -> None:
        '''鼠标单击事件'''
        if event.button() == Qt.RightButton:
            return
        if type(event) == QMouseEvent:
            mousePressPos = event.pos()
            mouseScenePos = self.mapToScene(mousePressPos)
        else:
            mouseScenePos = event.scenePos()
            mousePressPos = self.mapFromScene(mouseScenePos)
        if self.topLeftCornerRect().contains(mousePressPos):
            self.dragFlag = "TOP_LEFT"
            self.dragDiff = mouseScenePos - self.sceneTopLeft()
            return

        if self.topRightCornerRect().contains(mousePressPos):
            self.dragFlag = "TOP_RIGHT"
            self.dragDiff = mouseScenePos - self.sceneTopRight()
            return

        if self.bottomLeftCornerRect().contains(mousePressPos):
            self.dragFlag = "BOTTOM_LEFT"
            self.dragDiff = mouseScenePos - self.sceneBottomLeft()
            return

        if self.bottomRightCornerRect().contains(mousePressPos):
            self.dragFlag = "BOTTOM_RIGHT"
            self.dragDiff = mouseScenePos - self.sceneBottomRight()
            return
        if self.type == '圆环':
            if self.innerTopLeftCornerRect().contains(mousePressPos):
                self.dragFlag = "INNER_TOP_LEFT"
                self.dragDiff = mouseScenePos - self.innerSceneTopLeft()
                return

            if self.innerTopRightCornerRect().contains(mousePressPos):
                self.dragFlag = "INNER_TOP_RIGHT"
                self.dragDiff = mouseScenePos - self.innerSceneTopRight()
                return

            if self.innerBottomLeftCornerRect().contains(mousePressPos):
                self.dragFlag = "INNER_BOTTOM_LEFT"
                self.dragDiff = mouseScenePos - self.innerSceneBottomLeft()
                return

            if self.innerBottomRightCornerRect().contains(mousePressPos):
                self.dragFlag = "INNER_BOTTOM_RIGHT"
                self.dragDiff = mouseScenePos - self.innerSceneBottomRight()
                return
        # 旋转
        # if self.type == '矩形':
        #     if self.rotateCornerRect().contains(mousePressPos):
        #         self.dragFlag = "ROTATE"
        #         self.lastMouseMovePos = mousePressPos
        #         self.dragDiff = mouseScenePos
        #         return
        if self.centerRect().contains(mousePressPos):
            self.dragFlag = "CENTER"

            self.dragDiff = mouseScenePos - self.sceneTopLeft()
            return

    def mouseMoveEvent(self, event):
        '''选取框拖动缩放'''
        # if self.id != 'activeBox': # 非激活图元无法操作
        #     return None
        if type(event) == QMouseEvent:
            mouseMovePos = event.pos()
            # mouseMovePos = self.mapToScene(mouseMovePos)
        else:
            mouseMovePos = event.scenePos()

        xMinLimit = self.limitRect.x()
        xMaxLimit = xMinLimit + self.limitRect.width()
        yMinLimit = self.limitRect.y()
        yMaxLimit = yMinLimit + self.limitRect.height()
        minWidth = self.minSize.width()
        minHeight = self.minSize.height()

        self.prepareGeometryChange()  # 在几何变化之前准备几何图形的修改

        if self.dragFlag == "TOP_LEFT":
            sceneTopLeft = mouseMovePos - self.dragDiff
            sceneBottomRight = self.sceneBottomRight()

            curTLX = sceneTopLeft.x() if sceneTopLeft.x() > xMinLimit else xMinLimit
            curTLX = curTLX if sceneBottomRight.x() - curTLX > minWidth else sceneBottomRight.x() - minWidth
            curTLY = sceneTopLeft.y() if sceneTopLeft.y() > yMinLimit else yMinLimit
            curTLY = curTLY if sceneBottomRight.y() - curTLY > minHeight else sceneBottomRight.y() - minHeight

            if self.type == '矩形':
                self.size = QSizeF(sceneBottomRight.x() - curTLX, sceneBottomRight.y() - curTLY)
                self.setPos(QPointF(curTLX, curTLY))
            elif self.type == '圆形' or self.type == '圆环':
                old_size = self.size
                self.size = QSizeF(sceneBottomRight.y() - curTLY, sceneBottomRight.y() - curTLY)
                self.size = self.setRoundSize(self.size)
                self.setPos(QPointF((self.sceneTopLeft().x() - (self.size.width() - old_size.width()) / 2),
                                    (self.sceneTopLeft().y() - (self.size.height() - old_size.height()) / 2)))
                if self.type == '圆环':
                    scale = self.size.width() / old_size.width()
                    self.innerSize = self.innerSize * scale
        elif self.dragFlag == "INNER_TOP_LEFT":
            sceneTopLeft = mouseMovePos - self.dragDiff
            sceneBottomRight = self.innerSceneBottomRight()

            curTLY = sceneTopLeft.y() if sceneTopLeft.y() > yMinLimit else yMinLimit
            curTLY = curTLY if sceneBottomRight.y() - curTLY > minHeight else sceneBottomRight.y() - minHeight

            self.innerSize = QSizeF(sceneBottomRight.y() - curTLY, sceneBottomRight.y() - curTLY)
            self.innerSize = self.setRoundSize(self.innerSize)

        elif self.dragFlag == "TOP_RIGHT":
            sceneTopRight = mouseMovePos - self.dragDiff
            sceneBottomLeft = self.sceneBottomLeft()

            curTRX = sceneTopRight.x() if sceneTopRight.x() < xMaxLimit else xMaxLimit
            curTRX = curTRX if curTRX - sceneBottomLeft.x() > minWidth else sceneBottomLeft.x() + minWidth

            curTRY = sceneTopRight.y() if sceneTopRight.y() > yMinLimit else yMinLimit
            curTRY = curTRY if sceneBottomLeft.y() - curTRY > minHeight else sceneBottomLeft.y() - minHeight

            if self.type == '矩形':
                self.size = QSizeF(curTRX - sceneBottomLeft.x(), sceneBottomLeft.y() - curTRY)
                self.setPos(QPointF(sceneBottomLeft.x(), curTRY))
            elif self.type == '圆形' or self.type == '圆环':
                old_size = self.size
                self.size = QSizeF(curTRX - sceneBottomLeft.x(), curTRX - sceneBottomLeft.x())
                self.size = self.setRoundSize(self.size)
                self.setPos(QPointF(self.sceneTopLeft().x(),
                                    (self.sceneTopLeft().y() - (self.size.height() - old_size.height()) / 2)))
                if self.type == '圆环':
                    scale = self.size.width() / old_size.width()
                    self.innerSize = self.innerSize * scale
        elif self.dragFlag == "INNER_TOP_RIGHT":
            sceneTopRight = mouseMovePos - self.dragDiff
            sceneBottomLeft = self.innerSceneBottomLeft()

            curTRX = sceneTopRight.x() if sceneTopRight.x() < xMaxLimit else xMaxLimit
            curTRX = curTRX if curTRX - sceneBottomLeft.x() > minWidth else sceneBottomLeft.x() + minWidth

            self.innerSize = QSizeF(curTRX - sceneBottomLeft.x(), curTRX - sceneBottomLeft.x())
            self.innerSize = self.setRoundSize(self.innerSize)

        elif self.dragFlag == "BOTTOM_LEFT":
            sceneBottomLeft = mouseMovePos - self.dragDiff
            sceneTopRight = self.sceneTopRight()

            curBLX = sceneBottomLeft.x() if sceneBottomLeft.x() > xMinLimit else xMinLimit
            curBLX = curBLX if sceneTopRight.x() - curBLX > minWidth else sceneTopRight.x() - minWidth

            curBLY = sceneBottomLeft.y() if sceneBottomLeft.y() < yMaxLimit else yMaxLimit
            curBLY = curBLY if curBLY - sceneTopRight.y() > minHeight else sceneTopRight.y() + minHeight

            if self.type == '矩形':
                self.size = QSizeF(sceneTopRight.x() - curBLX, curBLY - sceneTopRight.y())
                self.setPos(QPointF(curBLX, sceneTopRight.y()))
            elif self.type == '圆形' or self.type == '圆环':
                old_size = self.size
                self.size = QSizeF(sceneTopRight.x() - curBLX, sceneTopRight.x() - curBLX)
                self.size = self.setRoundSize(self.size)
                self.setPos(QPointF((self.sceneTopLeft().x() - (self.size.width() - old_size.width())),
                                    (self.sceneTopLeft().y() - (self.size.height() - old_size.height()) / 2)))
                if self.type == '圆环':
                    scale = self.size.width() / old_size.width()
                    self.innerSize = self.innerSize * scale
        elif self.dragFlag == "INNER_BOTTOM_LEFT":
            sceneBottomLeft = mouseMovePos - self.dragDiff
            sceneTopRight = self.sceneTopRight()

            curBLX = sceneBottomLeft.x() if sceneBottomLeft.x() > xMinLimit else xMinLimit
            curBLX = curBLX if sceneTopRight.x() - curBLX > minWidth else sceneTopRight.x() - minWidth

            self.innerSize = QSizeF(sceneTopRight.x() - curBLX, sceneTopRight.x() - curBLX)
            self.innerSize = self.setRoundSize(self.innerSize)


        elif self.dragFlag == "BOTTOM_RIGHT":
            sceneBottomRight = mouseMovePos - self.dragDiff
            sceneTopLeft = self.sceneTopLeft()

            curBRX = sceneBottomRight.x() if sceneBottomRight.x() < xMaxLimit else xMaxLimit
            curBRX = curBRX if curBRX - sceneTopLeft.x() > minWidth else sceneTopLeft.x() + minWidth

            curBRY = sceneBottomRight.y() if sceneBottomRight.y() < yMaxLimit else yMaxLimit
            curBRY = curBRY if curBRY - sceneTopLeft.y() > minHeight else sceneTopLeft.y() + minHeight

            if self.type == '矩形':
                self.size = QSizeF(curBRX - sceneTopLeft.x(), curBRY - sceneTopLeft.y())
                self.setPos(sceneTopLeft)
            elif self.type == '圆形' or self.type == '圆环':
                old_size = self.size
                self.size = QSizeF(curBRY - sceneTopLeft.y(), curBRY - sceneTopLeft.y())
                self.size = self.setRoundSize(self.size)
                self.setPos(QPointF((self.sceneTopLeft().x() - (self.size.width() - old_size.width()) / 2),
                                    self.sceneTopLeft().y()))
                if self.type == '圆环':
                    scale = self.size.width() / old_size.width()
                    self.innerSize = self.innerSize * scale
        elif self.dragFlag == "INNER_BOTTOM_RIGHT":
            sceneBottomRight = mouseMovePos - self.dragDiff
            sceneTopLeft = self.sceneTopLeft()

            curBRY = sceneBottomRight.y() if sceneBottomRight.y() < yMaxLimit else yMaxLimit
            curBRY = curBRY if curBRY - sceneTopLeft.y() > minHeight else sceneTopLeft.y() + minHeight

            self.innerSize = QSizeF(curBRY - sceneTopLeft.y(), curBRY - sceneTopLeft.y())
            self.innerSize = self.setRoundSize(self.innerSize)
        # 旋转
        # elif self.dragFlag == 'ROTATE': # 旋转
        #     originPos = self.centerRect().center() # 设置中心点为旋转点
        #     # 从原点延伸出去两条线，鼠标按下时的点和当前鼠标位置所在点的连线
        #     p = QLineF(originPos, self.mapFromScene(self.dragDiff))
        #     p1 = QLineF(originPos, self.mapFromScene(self.lastMouseMovePos))
        #     p2 = QLineF(originPos, self.mapFromScene(mouseMovePos))
        #     dRotateAngle = p2.angleTo(p1) # 旋转角度
        #     self.setTransformOriginPoint(originPos)
        #     # 计算当前旋转的角度
        #     dCurAngle = self.rotation() + dRotateAngle
        #     while dCurAngle > 360.0:
        #         dCurAngle -= 360.0
        #     self.setRotation(dCurAngle) # 设置旋转角度
        #     self.lastMouseMovePos = mouseMovePos

        elif self.dragFlag == "CENTER":  # 移动
            sceneTopLeft = mouseMovePos - self.dragDiff
            curTLX = sceneTopLeft.x() if sceneTopLeft.x() > xMinLimit else xMinLimit
            curTLX = curTLX if curTLX + self.size.width() < xMaxLimit else xMaxLimit - self.size.width()
            curTLY = sceneTopLeft.y() if sceneTopLeft.y() > yMinLimit else yMinLimit
            curTLY = curTLY if curTLY + self.size.height() < yMaxLimit else yMaxLimit - self.size.height()
            self.setPos(QPointF(curTLX, curTLY))
        self.update()

    def mouseReleaseEvent(self, event):
        '''鼠标释放事件'''
        self.dragFlag = None

    def setState(self, pos, size):
        self.setPos(pos)
        self.size = size

    def setSize(self, size):
        self.size = size

    def setLimit(self, limit: QRectF):
        self.limitRect = limit

    def getState(self):
        return self.pos(), self.size

    def getPos(self):
        return self.pos()

    def getCentral(self):
        return QPointF(self.pos().x() + self.getWidth() / 2, self.pos().y() + self.getHeight() / 2)

    def getWidth(self):
        return self.size.width()

    def getHeight(self):
        return self.size.height()

    def getScale(self):
        if self.type == '圆环':
            return self.size.width() / self.innerSize.width()
        else:
            return 1


class PlaybackWindow(QGraphicsView):
    # 定义信号
    _signal_Press_pos = pyqtSignal(int, int)
    _signal_Point = pyqtSignal(int, int)

    def __init__(self, parent):
        super().__init__(parent)
        """填充图形左上角为（0，0）"""
        #
        self.setStyleSheet(u"broder: none")
        self.setBackgroundBrush(QColor(10, 10, 10, 200))
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        #
        self.setScene(QGraphicsScene())
        self.playbackItem = QGraphicsPixmapItem()  # 填充图形
        self.playbackItem.setPos(0, 0)
        self.scene().addItem(self.playbackItem)

        # self.setMouseTracking(True)  # 开启鼠标追踪

        self.isImg = None  # QImage
        self.curViewSize = None  # 存放窗口的当前大小
        self.curPlaySize = None  # 存放图片当前的实际播放大小
        self.lastPlaySize = None  # 存放图片当前的实际播放大小
        self.initPlaySize = None  # 存放窗口大小改变之前的图片大小
        self.scaleBy = 'width'  # 粗放是基于宽度，还是高度进行的缩放
        self.ponit_number = None  # 第几位标定点
        self.temp_path = None # 图像路径
        self.show_items = [] # 识别框
        self.text_items = [ ] # 识别框文本

        self.timerdict = {}  # 存储定时器的字典

        self.scene().setItemIndexMethod(QGraphicsScene.NoIndex)


    def showImgpath(self, temp_path=None):
        '''显示图片'''
        if not temp_path:
            temp_path = globalsdynamic.temp_path
        if temp_path:
            image = QImage(temp_path)
            self.initPlaySize = QSizeF(image.width(), image.height())
            self.lastPlaySize = self.initPlaySize
            self.temp_path = temp_path
            self.isImg = image

            self.updatePlayBackItem()

            # # 数据库保存
            # globalsdynamic.db_child.insert_data('View', {
            #     'name' : 'View',
            #     'curPlaySizeW': int(self.curPlaySize.width()),
            #     'curPlaySizeH': int(self.curPlaySize.height())
            # })

            self.displayImg()


    def displayImg(self,isImg=None,temp_path=None):
        ''' 更新图片'''
        if isinstance(self.temp_path,str):
            # 数据库读取
            # result = globalsdynamic.db_child.query_data_table('View')
            # result = result[0] if result else result
            # self.curPlaySize = QSizeF(float(result[1]),float(result[2]))

            if isImg :
                self.isImg = isImg


            # self.isImg.scaled(int(self.curPlaySize.width()), int(self.curPlaySize.height()), Qt.IgnoreAspectRatio,
            #               Qt.SmoothTransformation)  # 缩放图片

            # 缩放图片 有损清晰度
            # imageReader = QImageReader(self.temp_path)
            # imageReader.setScaledSize(QSize(int(self.curPlaySize.width()), int(self.curPlaySize.height())))
            # self.isImg = imageReader.read()

            self.isImg = self.isImg.scaled(int(self.curPlaySize.width()), int(self.curPlaySize.height()), Qt.IgnoreAspectRatio,
                          Qt.SmoothTransformation)
            pixmap = QPixmap.fromImage(self.isImg)
            # 设置平滑转换算法为保持清晰度
            self.playbackItem.setTransformationMode(Qt.SmoothTransformation)
            self.playbackItem.setPixmap(pixmap)



    # def delImg(self):

    def addText(self, text: str, pos: QPointF = QPointF(100, 100),size: int = 100) -> object:
        """新建文字"""
        # 创建文本项并设置文本内容和位置
        # item = QGraphicsTextItem(text)
        item = QGraphicsTextItem('哈后来赛欧很多都是')
        # 设置文本项的字体大小
        font = item.font()
        font.setPointSize(size)
        item.setFont(font)
        item.setPos(pos)

        # 将文本项添加到场景中
        self.scene().addItem(item)


    def addNewPoint(self, id="activeBox", type='矩形', pos=None, size=20):
        """
        新建标定点

        :param id: 图形的it
        :param type: 图形的类别
        :param pos: 图形中心点坐标 即图像标定点的坐标(x,y)
        :param size : 图形的大小 int
        """
        if self.isImg is None:
            return None

        item = self.getSelection(id)
        if not pos:
            pos = self.playbackItem.pos() + QPointF(self.curPlaySize.width() / 2, self.curPlaySize.height() / 2)
        else:
            pos = QPointF(pos[0], pos[1])
            self.updateScaleRatio()
            pos = pos / self.initscaleRatio - QPointF(size / 2, size / 2) + self.playbackItem.pos()
        if not item:
            item = SelectionBox(
                id=id,
                sort='标定点',
                pos=pos,
                size=QSizeF(size, size),
                centerPen=QPen(Qt.blue, 2),
                limitRect=QRectF(self.playbackItem.pos(), self.curPlaySize),
                type=type,
            )
            self.scene().addItem(item)
        # item.setActive(True)
        # self.setactiveItem(item)
        item.set_active()
        # item.setZValue(1)
        # item = self.getSort('标定点')
        # if item:
        #     item.setZValue(0)

    def addNewSelection(self, id="SelectionBox", type='矩形'):
        '''新建选取框'''
        if self.isImg is None:
            return None
        item = self.getSort('选取框')
        if item and item.type != type:  # 同形状的不会重新创建
            self.scene().removeItem(item)
            item = None
        if not item:  # 只能同时存在一个选取框=
            pos = self.playbackItem.pos() + QPointF(self.curPlaySize.width() / 4, self.curPlaySize.height() / 4)
            size = self.curPlaySize / 2
            limitRect = QRectF(self.playbackItem.pos(), self.curPlaySize)
            item = SelectionBox(
                id=id,
                pos=pos,
                size=size,
                limitRect=limitRect,
                type=type,
            )
            self.scene().addItem(item)
        # item.setActive(True)
        # self.setactiveItem(item)
        item.set_active()
        # item.setZValue(1)
        # item = self.getSort('掩码')
        # if item:
        #     item.setZValue(0)

    def addNewMask(self, id="activeBox", type='矩形',pos=None, size=None, typeOne = True):
        '''新建图片掩码'''
        if self.isImg is None:
            return None
        item = self.getSort('掩码')
        if not typeOne or (item and item.type != type):  # 同形状的不会重新创建
            self.scene().removeItem(item)
            item = None
        if not isinstance(pos,QPointF):
            pos = self.playbackItem.pos()
        if not isinstance(size,QSizeF):
            size=self.curPlaySize
        if not item:  # 只能同时存在一个掩码
            item = SelectionBox(
                id=id,
                sort='掩码',
                pos=pos,
                size=size,
                centerPen=QPen(Qt.blue, 2),
                limitRect=QRectF(self.playbackItem.pos(), self.curPlaySize),
                type=type,
            )
            self.scene().addItem(item)
        # item.setActive(True)
        # self.setactiveItem(item)
        item.set_active()
        # item.setZValue(1)
        # item = self.getSort('选取框')
        # if item:
        #     item.setZValue(0)

    def turnNewShowBox(self, box, move=QPoint(0, 0), id='activeBox'):
        """
        转换显示框

        :param box: ([y1], [x1], [y2], [x2])
        :param move: 掩码左上角的坐标
        """
        # box
        if self.isImg is None:
            return None
        try:
            self.updateScaleRatio()
            id = 'NewShowBox' + str(id)

            # 将显示框在图像上的左上角和右下角坐标转换为在item坐标系上的坐标
            Y1, X1, Y2, X2 = box
            # move_x = move.x()
            # move_y = move.y()
            # y1 = int((Y1 + move_y) / self.initscaleRatio)
            # x1 = int((X1 + move_x) / self.initscaleRatio)
            # y2 = int((Y2 + move_y) / self.initscaleRatio)
            # x2 = int((X2 + move_x) / self.initscaleRatio)
            y1 = Y1 / self.initscaleRatio
            x1 = X1 / self.initscaleRatio
            y2 = Y2 / self.initscaleRatio
            x2 = X2 / self.initscaleRatio

            return x1,y1,x2,y2

        except Exception as e:
            print(e)

    def addShowBoxText(self,item,text,pos='center'):
        # 识别框文本显示
        try:
            text = QGraphicsTextItem(text, item)
            text.setPos(0, 10)
            text.setFont(QFont('Arial', item.boundingRect().width()/16+item.boundingRect().height()/16))
            text.setDefaultTextColor(QColor('orange'))
            text.setTextWidth(item.boundingRect().width())  # 根据矩形item的宽度自动换行
            # 计算文本的高度
            text_height = text.boundingRect().height()
            # 设置文本的位置使其居中
            if pos == 'center':
                text.setPos(item.boundingRect().center().x() - text.boundingRect().width() / 2,
                            item.boundingRect().center().y() - text_height / 2)
            elif pos == 'up':
                text.setPos(item.boundingRect().center().x() - text.boundingRect().width() / 2 )
            elif pos == 'down':
                text.setPos(item.boundingRect().center().x() - text.boundingRect().width() / 2,
                            item.boundingRect().center().y() - text_height/2)
            self.text_items.append(text)
        except Exception as e:
            print(e)
    def addNewShowBox(self,x1,y1,x2,y2,text:str):
        """新增识别框"""
        # num = datetime.now().strftime('%Y-%m-%d-%H-%M-%S.%f')  # 当前系统时间
        item = SelectionBox(
            id=str(id),
            centerPen=QPen(Qt.green, 3),
            cornerSize=QSizeF(0, 0),
            pos=self.playbackItem.pos() + QPointF(x1, y1),
            size=QSizeF(x2 - x1, y2 - y1),
            limitRect=QRectF(self.playbackItem.pos(), self.curPlaySize)
        )

        self.addShowBoxText(item, text+'\n')

        item.setEnabled(False)  # 是否禁用
        self.scene().addItem(item)

        self.show_items.append(item)
        # # 定时删除
        # self.timerdict[id] = QTimer()
        # self.timerdict[id].timeout.connect(lambda: self.delete_item(id))
        # self.timerdict[id].start(2000)  # 2秒后删除item
    def clearShowBox(self):
        """清空识别框"""
        for item in self.show_items:
            self.scene().removeItem(item) if item in self.scene().items()  else []
        self.show_items = []
    def clearShowBoxText(self):
        """清空识别框文本"""
        for item in self.text_items:
            self.scene().removeItem(item) if item in self.scene().items() else []
        self.text_items = []
    def get_active(self):
        """获取激活的item"""
        for item in self.scene().items():
            if isinstance(item, SelectionBox) and item.isEnabled():
                return item
        return None

    def getSelection(self, id):
        '''获取特定ip的item'''
        for item in self.scene().items():
            if isinstance(item, SelectionBox) and item.id == id:
                return item
        return None

    def getType(self, type):
        '''获取特定形状的item'''
        for item in self.scene().items():
            if isinstance(item, SelectionBox) and item.type == type:
                return item
        return None

    def getSort(self, sort):
        '''获取特定类型的item'''
        for item in self.scene().items():
            if isinstance(item, SelectionBox) and item.sort == sort:
                return item
        return None

    def getSelectionScale(self, id):
        '''获取圆环外/内圆半径比例'''
        selection = self.getType(id)
        if selection is None:
            return None
        return selection.getScale()

    def getSelectionSize(self, selection):
        '''获取选取框大小'''
        if selection is None:
            return None
        height, width = self.isImg.height(), self.isImg.width()

        return QSizeF(
            width * selection.getWidth() / self.curPlaySize.width(),
            height * selection.getHeight() / self.curPlaySize.height(),
        )

    def getSelectionPos(self, selection):
        '''获取选取框位置'''
        if selection is None:
            return None
        height, width = self.isImg.height(), self.isImg.width()
        return QPointF(
            (selection.pos().x() - self.playbackItem.pos().x()) * width / self.curPlaySize.width(),
            (selection.pos().y() - self.playbackItem.pos().y()) * height / self.curPlaySize.height(),
        )

    def getImg(self, item, pos, size, type='矩形'):
        '''截取图片'''
        # 将大小和位置转换为整数值
        self.updateScaleRatio()
        angle = item.rotation()  # 截取框旋转角度
        width = int(size.width())  # # 截取框宽高
        height = int(size.height())
        x = int(pos.x())  # 截取框左上角
        y = int(pos.y())
        if isinstance(self.temp_path, str):
            image = QImage(self.temp_path)
        else:
            image = self.isImg


        # # 图元坐标转换为图片坐标
        x = x * self.initscaleRatio
        y = y * self.initscaleRatio
        width = width * self.initscaleRatio
        height = height * self.initscaleRatio
        # 截图
        cropped_image = image.copy(x, y, width, height)

        # 旋转
        # self.scalew = image.width() / self.isImg.width()
        # self.scaleh = image.height() / self.isImg.height
        # if angle:
        #     # 计算旋转后的截取框的中心点坐标
        #     center_x = x + width / 2
        #     center_y = y + height / 2
        #
        #     # 计算旋转后的截取框的四个角点坐标
        #     angle_rad = math.radians(angle)
        #     cos_theta = math.cos(angle_rad)
        #     sin_theta = math.sin(angle_rad)
        #     x1 = center_x + (x - center_x) * cos_theta - (y - center_y) * sin_theta
        #     y1 = center_y + (x - center_x) * sin_theta + (y - center_y) * cos_theta
        #     x2 = center_x + (x + width - center_x) * cos_theta - (y - center_y) * sin_theta
        #     y2 = center_y + (x + width - center_x) * sin_theta + (y - center_y) * cos_theta
        #     x3 = center_x + (x + width - center_x) * cos_theta - (y + height - center_y) * sin_theta
        #     y3 = center_y + (x + width - center_x) * sin_theta + (y + height - center_y) * cos_theta
        #     x4 = center_x + (x - center_x) * cos_theta - (y + height - center_y) * sin_theta
        #     y4 = center_y + (x - center_x) * sin_theta + (y + height - center_y) * cos_theta
        #
        #     # 计算旋转后的截取框的最小外接矩形
        #     min_x = min(x1, x2, x3, x4)
        #     min_y = min(y1, y2, y3, y4)
        #     max_x = max(x1, x2, x3, x4)
        #     max_y = max(y1, y2, y3, y4)
        #     rotated_width = max_x - min_x
        #     rotated_height = max_y - min_y
        #
        #     # 截取旋转后的图片
        #     cropped_image = crop_quadrilateral(image,(x1,y1),(x2,y2),(x3,y3),(x4,y4))
        if type == '矩形':
            # 截取图片
            return cropped_image, QPoint(x, y)
        elif type == '圆形':
            # 截取图片
            cropped_image = crop_circle(cropped_image)
            return cropped_image, QPoint(x, y)
        elif type == '圆环':
            cropped_image = crop_ring(cropped_image, self.getSelectionScale('圆环'))
            return cropped_image, QPoint(x, y)

    def getSelectionImg(self, type='矩形'):
        '''获取选取框框选的图片'''
        try:
            item = self.getSort('选取框')
            pos = self.getSelectionPos(item)
            size = self.getSelectionSize(item)
            if size is None or pos is None:
                return None
            cropped_image, pos = self.getImg(item, pos, size, type)
            return cropped_image
        except Exception as e:
            print(e)

    def getMaskImg(self, type='矩形'):
        """
        获取掩码图片和掩码左上角的坐标
        """
        if not self.getSort('掩码'):
            return QImage(self.temp_path), QPoint(0, 0),QPoint(0, 0),None,1,type
        item = self.getSort('掩码')
        pos = self.getSelectionPos(item) # 在item中填充图形左上角为（0，0）
        size = self.getSelectionSize(item)
        # if size is None or pos is None:
        #     return None
        cropped_image, pos = self.getImg(item, pos, size, type)
        item_pos = QPointF(item.pos().x()-self.playbackItem.pos().x() , item.pos().y()-self.playbackItem.pos().y())# 在item中图像左上角为（0，0）

        return cropped_image, item_pos,pos, size , self.initscaleRatio , type

    def getCoordinates(self, event):
        '''点击显示坐标'''
        if self.scaleBy is None:
            return
        if self.scaleBy == "width":
            x = event.pos().x()
            y = event.pos().y() - int((self.curViewSize.height() - self.isImg.height()) / 2)
        elif self.scaleBy == "height":
            x = event.pos().x() - int((self.curViewSize.width() - self.isImg.width()) / 2)
            y = event.pos().y()
        return x, y

    def item_to_img(self, item_point):
        '''item坐标转图像坐标'''
        self.updateScaleRatio()
        img_point = self.initscaleRatio * item_point
        return img_point
    def img_to_item(self, img_point):
        '''图像坐标转item坐标'''
        self.updateScaleRatio()
        item_point = img_point / self.initscaleRatio
        return item_point

    def updatePlayBackItem(self):
        '''更新图片尺寸'''
        if self.curPlaySize:
            self.lastPlaySize = self.curPlaySize
        fh, fw = self.isImg.height(), self.isImg.width()
        ww = self.curViewSize.width()
        wh = self.curViewSize.height()
        try:
            scaledSize, self.scaleBy = KeepAspectScale(fw, fh, ww, wh)
        except:
            print('图像丢失')
            scaledSize = [float(ww),float(wh)]
        self.curPlaySize = QSizeF(*scaledSize)

        self.playbackItem.setPos(
            QPointF((ww - scaledSize[0]) / 2, (wh - scaledSize[1]) / 2))

    def updateScaleRatio(self):
        '''更新图片更新前后比例'''
        if self.scaleBy == "width":
            self.initscaleRatio = self.initPlaySize.width() / self.curPlaySize.width()  # 初始图片大小与现在播放大小的比例
            self.lastscaleRatio = self.lastPlaySize.width() / self.curPlaySize.width()  # 上一次播放大小与现在播放大小的比例
        elif self.scaleBy == "height":
            self.initscaleRatio = self.initPlaySize.height() / self.curPlaySize.height()
            self.lastscaleRatio = self.lastPlaySize.width() / self.curPlaySize.width()  # 上一次播放大小与现在播放大小的比例

    def delete_item(self, id):
        '''定时器事件 删除item'''
        self.timerdict[id].stop()
        self.scene().removeItem(self.getSelection(str(id)))

    def clear(self):
        '''清除所有item 掩码除外'''
        self.show_items = []
        self.clearShowBoxText()

        for key in self.timerdict.keys():
            self.timerdict[key].stop()
        lena = len(self.scene().items())
        for item in self.scene().items():
            if isinstance(item, SelectionBox) and item != self.getSort('掩码'):
                item.scene().removeItem(item)

    def mousePressEvent(self, event):
        '''鼠标点击事件'''
        super().mousePressEvent(event)
        try:
            x, y = self.getCoordinates(event)
            # 发射信号
            self._signal_Press_pos.emit(x, y)

        except Exception as e:
            print(e)

    def mouseMoveEvent(self, event):
        '''鼠标移动事件'''
        super().mouseMoveEvent(event)
        x, y = self.getCoordinates(event)
        # 发射信号
        self._signal_Press_pos.emit(x, y)

        item = self.get_active()
        if item and isinstance(item, SelectionBox) and item.type == '标定':
            self.updateScaleRatio()
            central = (item.getCentral() - self.playbackItem.pos()) * self.initscaleRatio
            x = central.x()
            y = central.y()
            self._signal_Point.emit(x, y)

    def resizeEvent(self, event):
        self.curViewSize = event.size()
        # 创建一个QPointF对象
        point = QPointF(0, 0)

        # 获取curViewSize的宽度和高度
        curViewSize = self.curViewSize
        width = curViewSize.width()
        height = curViewSize.height()

        # 创建一个QRectF对象
        rect = QRectF(point, QPointF(width, height))
        # rect = QRectF(QPointF(0, 0), self.curViewSize)
        self.setSceneRect(rect)

        if self.isImg is None:
            return
        #
        lastplaybackItemPos = self.playbackItem.pos()  # 未变形前框的坐标
        #
        self.updatePlayBackItem()
        #
        playbackItemNewPos = self.playbackItem.pos()
        #
        self.displayImg()

        # 处理内部的框
        self.updateScaleRatio()
        for item in self.scene().items():
            if isinstance(item, SelectionBox):
                x = item.getPos().x() - lastplaybackItemPos.x()
                y = item.getPos().y() - lastplaybackItemPos.y()
                w = item.getWidth()
                h = item.getHeight()
                item.setLimit(QRectF(playbackItemNewPos, self.curPlaySize))
                if item.type == '标定':
                    item.setState(
                        QPointF(x / self.lastscaleRatio + playbackItemNewPos.x() + w / 2 / self.lastscaleRatio - w / 2,
                                y / self.lastscaleRatio + playbackItemNewPos.y() + h / 2 / self.lastscaleRatio - h / 2),
                        QSizeF(w, h)
                    )
                else:
                    item.setState(
                        QPointF(x / self.lastscaleRatio + playbackItemNewPos.x(),
                                y / self.lastscaleRatio + playbackItemNewPos.y()),
                        QSizeF(w / self.lastscaleRatio, h / self.lastscaleRatio)
                    )

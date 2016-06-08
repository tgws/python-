#!/usr/bin/python
# -*- coding: utf-8 -*-
import easygui as gui
title="GAME"
gui.msgbox("点击开始",title)
choices=["柠檬","bananna","strawberry"]
flavor=gui.buttonbox("从下面挑出你最喜欢的冰激凌口味：",title,choices)
gui.msgbox("你选择了"+str(flavor))



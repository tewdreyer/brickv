# -*- coding: utf-8 -*-  
"""
Current Plugin
Copyright (C) 2011 Olaf Lüke <olaf@tinkerforge.com>

current.py: Current Plugin Implementation

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation; either version 2 
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from plugin_system.plugin_base import PluginBase
from bindings import ip_connection
from plot_widget import PlotWidget

from PyQt4.QtGui import QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt4.QtCore import pyqtSignal, Qt
        
from bindings import bricklet_current12
        
class CurrentLabel(QLabel):
    def setText(self, text):
        text = "Current: " + text + " A"
        super(CurrentLabel, self).setText(text)
    
class Current12(PluginBase):
    qtcb_current = pyqtSignal(int)
    qtcb_over = pyqtSignal()
    
    def __init__ (self, ipcon, uid):
        PluginBase.__init__(self, ipcon, uid)
        
        self.cur = bricklet_current12.Current12(self.uid)
        self.ipcon.add_device(self.cur)
        self.version = '.'.join(map(str, self.cur.get_version()[1]))
        
        self.qtcb_current.connect(self.cb_current)
        self.cur.register_callback(self.cur.CALLBACK_CURRENT,
                                   self.qtcb_current.emit) 
        
        self.qtcb_over.connect(self.cb_over)
        self.cur.register_callback(self.cur.CALLBACK_OVER_CURRENT,
                                   self.qtcb_over.emit) 
        
        self.current_label = CurrentLabel('Current: ')
        self.over_label = QLabel('Over Current: No')
        self.calibrate_button = QPushButton('Calibrate')
        self.calibrate_button.pressed.connect(self.calibrate_pressed)
        
        self.current_value = 0
        
        plot_list = [['', Qt.red, self.get_current_value]]
        self.plot_widget = PlotWidget('Current [mA]', plot_list)
        
        layout_h1 = QHBoxLayout()
        layout_h1.addStretch()
        layout_h1.addWidget(self.current_label)
        layout_h1.addStretch()

        layout_h2 = QHBoxLayout()
        layout_h2.addStretch()
        layout_h2.addWidget(self.over_label)
        layout_h2.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(layout_h1)
        layout.addLayout(layout_h2)
        layout.addWidget(self.plot_widget)
        layout.addWidget(self.calibrate_button)

    def start(self):
        try:
            self.cb_current(self.cur.get_current())
            self.cur.set_current_callback_period(100)
        except ip_connection.Error:
            return
        
        self.plot_widget.stop = False
        
    def stop(self):
        try:
            self.cur.set_current_callback_period(0)
        except ip_connection.Error:
            pass
            
        self.plot_widget.stop = True

    @staticmethod
    def has_name(name):
        return 'Current12 Bricklet' in name 

    def get_current_value(self):
        return self.current_value

    def cb_current(self, current):
        self.current_value = current
        self.current_label.setText(str(current/1000.0)) 
        
    def cb_over(self):
        self.over_label.setText('Over Current: Yes')
        
    def calibrate_pressed(self):
        try:
            self.cur.calibrate()
        except ip_connection.Error:
            return
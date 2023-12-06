#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: uis-e3t
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ENVOLVENTECOMPLEJAPM import ENVOLVENTECOMPLEJAPM  # grc-generated hier_block
from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import sip



class parte_4_b_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "uis-e3t", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("uis-e3t")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "parte_4_b_1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200e3
        self.fm = fm = 1e3
        self.fc = fc = 50e6
        self.Kp = Kp = 1
        self.GTX = GTX = 1
        self.Am = Am = 1
        self.Ac = Ac = 1

        ##################################################
        # Blocks
        ##################################################

        self._fc_range = Range(50e6, 2e9, 1e6, 50e6, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "frecuencia de la portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self._Kp_range = Range(0, 10, 1e-6, 1, 200)
        self._Kp_win = RangeWidget(self._Kp_range, self.set_Kp, "coeficiente Kp", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Kp_win)
        self._Ac_range = Range(0, 1, 1e-6, 1, 200)
        self._Ac_win = RangeWidget(self._Ac_range, self.set_Ac, "amplitud portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Ac_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(200e3)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            200e3, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            8192, #size
            window.WIN_HAMMING, #wintype
            0, #fc
            200e3, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._fm_range = Range(1e3, 200e3, 100, 1e3, 200)
        self._fm_win = RangeWidget(self._fm_range, self.set_fm, "frecuencia del mensaje ", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self.analog_sig_source_x_0 = analog.sig_source_f(200e3, analog.GR_COS_WAVE, 1000, 1, 0, 0)
        self._GTX_range = Range(0, 30, 1, 1, 200)
        self._GTX_win = RangeWidget(self._GTX_range, self.set_GTX, "ganancia del transmisor ", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._GTX_win)
        self.ENVOLVENTECOMPLEJAPM_0 = ENVOLVENTECOMPLEJAPM(
            Ac=(100e-3),
            Kp=1,
        )
        self._Am_range = Range(0, 1, 1e-6, 1, 200)
        self._Am_win = RangeWidget(self._Am_range, self.set_Am, "amplitud del mensaje ", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ENVOLVENTECOMPLEJAPM_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.ENVOLVENTECOMPLEJAPM_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ENVOLVENTECOMPLEJAPM_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ENVOLVENTECOMPLEJAPM_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "parte_4_b_1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_Kp(self):
        return self.Kp

    def set_Kp(self, Kp):
        self.Kp = Kp

    def get_GTX(self):
        return self.GTX

    def set_GTX(self, GTX):
        self.GTX = GTX

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am

    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac




def main(top_block_cls=parte_4_b_1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

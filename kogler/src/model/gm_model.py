"""
Model
"""

import requests
import xml.etree.ElementTree as ET


class Model(object):
    """
    This Class is the Model
    """

    def __init__(self, url="http://maps.googleapis.com/maps/api/directions/xml"):
        """ init

        :param url:
        """
        self.origin = ""
        self.dest = ""
        self.output = ""
        self.status = ""
        self.param = {}
        self.url = url

    def getData(self, origin, dest, mode, lang):
        if mode == "  Driving":
            self.param['mode'] = "driving"
        elif mode == "  Bicycling":
            self.param['mode'] = "bicycling"
        elif mode == "  Walking":
            self.param['mode'] = "walking"

        if lang == "  DE":
            self.param['language'] = "de"
        elif lang == "  EN":
            self.param['language'] = "en"
        elif lang == "  EL":
            self.param['language'] = "el"

        print(self.param)


        self.origin = origin
        self.dest = dest
        self._pushParam()
        xml = requests.get(self.url, self.param)

        if (self.getStatusFromXml(xml)) != "OK":
            print("Not OK")

        self.instr = self.getInstrFromXml(xml)
        self.time = self.getTimeFromXml(xml)
        self.status = self.getStatusFromXml(xml)

        return {'instr': self.instr,
                'time': self.time,
                'status':self.status
                }

    def getStatusFromXml(self, xml):
        root = ET.fromstring(xml.text)
        return root[0].text


    def getInstrFromXml(self, xml):
        root = ET.fromstring(xml.text)
        instr = ""
        for route in root.iter('route'):
            leg = route[1]
            i = 1
            for step in leg.findall('step'):
                if "<div " in str(step.find('html_instructions').text):
                    instr += "<br>" + step.find('html_instructions').text + "<br><br>"
                else:
                    instr += "Schritt (" + str(i) + ") -> " + step.find('html_instructions').text + "<br>" \
                             + "<div align='right''>Duration: " + step.find('duration')[1].text + "<br>" \
                             + "Distance: " + step.find('distance')[1].text + "</div>" \
                                                                              "<br>"
                i += 1
        return instr

    def getTimeFromXml(self, xml):
        root = ET.fromstring(xml.text)
        time = ""
        for route in root.iter('route'):
            leg = route[1]
            dur = leg.find('duration')[1].text
            dist = leg.find('distance')[1].text
            time += "Sie brauchen insgesamt " + dur + "<br>" \
                                                      "Bei einer Distanz von " + dist + "<br><br>"

        return time

    def _pushParam(self):
        self.param['origin'] = self.origin
        self.param['destination'] = self.dest
"""
Model Class
This class will make all necessary HTTP - Request and stores its
results in appropriate variables and attributes
"""

import requests
import xml.etree.ElementTree as ET


class Model(object):
    """
    This Class acts as the Model in an MVC - Concept
    All important data will be stored here
    for later use
    """

    def __init__(self, url="http://maps.googleapis.com/maps/api/directions/xml"):
        """ init - Method

        Initializes the Model Object
        it takes an url to invoke the REST Calls from

        :param url: URL for HTTP-Request
        """
        self.origin = ""
        self.dest = ""
        self.output = ""
        self.status = ""
        self.param = {}
        self.url = url

    def getData(self, origin, dest, mode, lang):
        """ getData - Method

        This method performs the HTTP-Request
        It takes all necessary parameters for a valid HTTP - Request

        :param origin: Start
        :param dest: Ziel
        :param mode: Modus, wlaking usw
        :param lang: Language
        :return: Tuple with [0]: instr, [1]: time, [2]: status
        """
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
        """ getStatus from Google Maps Api XML

        Returns the staus as a string

        :param xml: xml
        :return: string status
        """
        root = ET.fromstring(xml.text)
        return root[0].text


    def getInstrFromXml(self, xml):
        """ getInstrFromXml - Method

        Parses the instructions from the passed xml
        formats them to an string

        :param xml: Google Maps xml
        :return: Instructions as string
        """
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
        """ getTimeFromXml

        Formats the Duration as a string

        :param xml: Google Maps xml
        :return: String
        """
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
        """ set origin and dest to the params dicitionary
        :return:
        """
        self.param['origin'] = self.origin
        self.param['destination'] = self.dest
.. Google Maps RESTful documentation master file, created by
   sphinx-quickstart on Mon Nov 14 16:48:45 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GM-Form's documentation!
===================================

Bibliographic feild:
--------------------
   :Author: Anonym
   :organization: TGM Wien
   :date: 2016-12-11
   :revision: 1.0.1
   :version: 1.0


Contents:
---------

.. toctree::
   :maxdepth: 2

   controller
   model
   view

Usage:
------
*Controller*

>>> from kogler.src.controller.gm_controller import Controller
>>> # Starts the Application
>>> c = Controller()

*Model REST - Service*

>>> from kogler.src.model.gm_model import Model
>>> url = "http://maps.googleapis.com/maps/api/directions/xml"
>>> m = Model(url)
>>> origin = "Wien"
>>> dest = "Nussdorf"
>>> mode = "walking"
>>> lang = "DE"
>>> # Call getData with Parameters
>>> m.getData(origin, dest, mode, lang)

View:
=====

.. image:: _static/view.png
       :align: center


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


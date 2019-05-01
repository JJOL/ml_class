# Skin-Injuries-Diseases Detection and Helper System

Proyectos Similares o Inspirados para:
https://www.consalud.es/app-saludable/codigo-infarto_48170_102.html

State of the Art:
App DermaPhoto: Skin Disease Prediction 90%


Diseases:

Herpes:
* Herpes Simple Type I **
* Herpes Simple Type II **
* Herpes Zoster / Varicela Zoster **

* PSoriasis **
* Dermatitis Seborreica *
* Vitiligo **
* Tiñas (dermatofitosis) **

* Hematoma (Moreton) **

Piodermias:
* Impetigo *
* Hidroademitis (hidradenitis supurativa) **
* Folliculitis *
* Celulitis **
* Ectima *


Main Input:
An image of the affected zone

Auxiliary Input:
A vector of additional information
- Topografía (Codo, Brazos, Torzo, Cuello, Etc.) <- Fácil
- Morfologia (2 clusters, grande, irregular) <- Difícil
- Sintomas   (Dolor, Comezon, Ardor, Calor, Secresión) <- Medio


# Dependencies:
- virtualenv
- pip

- googleimagesdownload (for downloading image data sets)
- bottle (web server for swipe_filter)
- Pillow (for image processing)
- Tensorflow
- Keras

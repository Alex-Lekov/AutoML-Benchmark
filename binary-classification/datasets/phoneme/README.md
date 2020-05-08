The resources for this dataset can be found at https://www.openml.org/d/1489

Author: Dominique Van Cappel, THOMSON-SINTRA  
Source: [KEEL](http://sci2s.ugr.es/keel/dataset.php?cod=105#sub2), [ELENA](https://www.elen.ucl.ac.be/neural-nets/Research/Projects/ELENA/databases/REAL/phoneme/) - 1993  
Please cite: None  

The aim of this dataset is to distinguish between nasal (class 0) and oral sounds (class 1). Five different attributes were chosen to characterize each vowel: they are the amplitudes of the five first harmonics AHi, normalised by the total energy Ene (integrated on all the frequencies): AHi/Ene. The phonemes are transcribed as follows: sh as in she, dcl as in dark, iy as the vowel in she, aa as the vowel in dark, and ao as the first vowel in water.  

### Source

The current dataset was formatted by the KEEL repository, but originally hosted by the [ELENA Project](https://www.elen.ucl.ac.be/neural-nets/Research/Projects/ELENA/elena.htm#stuff). The dataset originates from the European ESPRIT 5516 project: ROARS. The aim of this project was the development and the implementation of a real time analytical system for French and Spanish speech recognition.  

### Relevant information

Most of the already existing speech recognition systems are global systems (typically Hidden Markov Models and Time Delay Neural Networks) which recognizes signals and do not really use the speech
specificities.  On the contrary, analytical systems take into account the articulatory process leading to the different phonemes of a given language, the idea being to deduce the presence of each of the
phonetic features from the acoustic observation.

The main difficulty of analytical systems is to obtain acoustical parameters sufficiantly reliable. These acoustical measurements must :

   - contain all the information relative to the concerned phonetic feature.
   - being speaker independent.
   - being context independent.
   - being more or less robust to noise.

The primary acoustical observation is always voluminous (spectrum x N different observation moments) and classification cannot been processed directly.

In ROARS, the initial database is provided by cochlear spectra, which may be seen as the output of a filters bank having a constant DeltaF/F0, where the central frequencies are distributed on a
logarithmic scale (MEL type) to simulate the frequency answer of the auditory nerves.  The filters outputs are taken every 2 or 8 msec (integration on 4 or 16 msec) depending on the type of phoneme
observed (stationary or transitory).  

The aim of the present database is to distinguish between nasal and
oral vowels. There are thus two different classes:

- Class 0 : Nasals  
- Class 1 : Orals        

This database contains vowels coming from 1809 isolated syllables (for example: pa, ta, pan,...). Five different attributes were chosen to characterize each vowel: they are the amplitudes of the five first harmonics AHi, normalised by the total energy Ene (integrated on all the frequencies): AHi/Ene. Each harmonic is signed: positive when it corresponds to a local maximum of the spectrum and negative otherwise.

Three observation moments have been kept for each vowel to obtain 5427 different instances: 

 - the observation corresponding to the maximum total energy Ene. 
   
 - the observations taken 8 msec before and 8 msec after the observation corresponding to this maximum total energy.

From these 5427 initial values, 23 instances for which the amplitude of the 5 first harmonics was zero were removed, leading to the 5404 instances of the present database. The patterns are presented in a random order.

### Past Usage  

Alinat, P., Periodic Progress Report 4, ROARS Project ESPRIT II- Number 5516, February 1993, Thomson report TS. ASM 93/S/EGS/NC/079  
    
Guerin-Dugue, A. and others, Deliverable R3-B4-P - Task B4: Benchmarks, Technical report, Elena-NervesII "Enhanced Learning for Evolutive Neural Architecture", ESPRIT-Basic Research Project  Number 6891, June 1995  

Verleysen, M. and Voz, J.L. and Thissen, P. and Legat, J.D., A statistical Neural Network for high-dimensional vector classification, ICNN'95 - IEEE International Conference on Neural Networks, November 1995, Perth, Western Australia.  
    
Voz J.L., Verleysen M., Thissen P. and Legat J.D., Suboptimal Bayesian classification by vector quantization with small clusters. ESANN95-European Symposium on Artificial Neural Networks, April 1995, M. Verleysen editor, D facto publications, Brussels, Belgium.  
    
Voz J.L., Verleysen M., Thissen P. and Legat J.D., A practical view of  suboptimal Bayesian classification, IWANN95-Proceedings of the International Workshop on Artificial Neural Networks, June 1995, Mira, Cabestany, Prieto editors, Springer-Verlag Lecture Notes in Computer Sciences, Malaga, Spain  

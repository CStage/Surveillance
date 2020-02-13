0. Introduction
1. Idea and Purpose
2. Code contributions and inspiration
3. Future steps

______________________________
0. Introduction
________________________________

This script was created in an attempt to get familiar with the OpenCV Python-library, while also developing something meaningful. It calculates the pythagorean distance between two frames, calculates the standard deviation and then starts recording when motion is detected.

______________________________
1. Idea and Purpose
________________________________

The idea came from a problem at my current residence (dorm), where individuals from other kitchens would sometimes steal beer or cleaning equipment from our storage room. We played around with the idea of some basic surveillance, and thus this script was developed. As of right now, it is just a prototype and would need some refinement before actual implementation. In our specific case it is set up to record motion and upload it as video-files to a OneDrive folder which we can then check for suspicious behavior, when we suspect that theft has taken place. As of yet, the ethics of the system are still being discussed and thus only small-scale tests have been conducted and the system has yet to be implemented.

______________________________
2. Code Contributions and Inspiration
________________________________
Some code borrowed from: https://software.intel.com/en-us/node/754940

Inspired by modern motion tracking systems and an interest in combatting theft in the dorm in an organized and harmless way.

______________________________
3. Future steps
________________________________
I have briefly considered implementing a face detection feature, so that the script can determine whether or not the person in frame is authorized to enter the room. Of course a new set of ethics would then have to be approved, but even if we decide not to implement it, I seek to try to create some facial detection software in the future.
# Unit 10: Markov chains

In this last unit we introduce Markov chains, a general class of random processes with many applications dealing with the evolution of dynamical systems. A Markov chain's defining feature implies that conditional on the current state of the process, its future and past evolutions are independent.

After introducing basic concepts using a simple queuing example, we will concentrate on the behavior of a Markov chain in the long run, that is after we let it evolve for a long time, and study under what conditions a Markov chain exhibits some sort of steady-state behavior, and under what conditions that behavior is independent of the initial starting state.

We will also look at a classical application of Markov chains and conclude by making use of all that we have learned in order to calculate some interesting quantities associated with short-term behaviors of Markov chains.

Printable transcript available [here](https://courses.edx.org/assets/courseware/v1/0fa38c83103635a23c7dc642fab6c82f/asset-v1:MITx+6.431x+1T2024+type@asset+block/transcripts_U10-Overview.pdf).

The material in this unit is covered in [Chapter 7](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/52) of the text.

The same material, in live lecture hall format, can be found on OCW ([Lecture 16](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-16-markov-chains-i/), [Lecture 17](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-17-markov-chains-ii/), [Lecture 18](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-18-markov-chains-iii/)) and YouTube ([Lecture 16](https://www.youtube.com/watch?v=IkbkEtOOC1Y), [Lecture 17](https://www.youtube.com/watch?v=ZulMqrvP-Pk), [Lecture 18](https://www.youtube.com/watch?v=HIMxdWDLEK8)).

# [Lecture 24: Finite-state Markov chains](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__24_Finite-state_Markov_chains)

In this lecture, we introduce discrete-time finite space Markov chains, first looking at a simple example of a checkout counter at a supermarket, then introducing the central notions of states, transition probabilities, the Markov property, and transition probability graphs.

Afterwards, we look at the question of predicting what would happen n steps in the future given the current state of our system. We define n-step transition probabilities and show how to calculate them efficiently. We also discuss what could happen when we let a Markov chain run for a very long time. We end this lecture by introducing the notions of recurrent and transient states and their importance in studying Markov chains in the long run.

Printable transcript available [here](https://courses.edx.org/assets/courseware/v1/adca1e6b2d8d243deade9d599d9a2ceb/asset-v1:MITx+6.431x+1T2024+type@asset+block/transcripts_L24-Overview.pdf).

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/93ef4b8076fd9e1dd7c8737535920f8c/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L24-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/933d36c15adae706e15ba25f18179abd/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L24-annotated-slides.pdf)

More information is given in [Sections 7.1-7.2](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/53) of the text.

# [Lecture 25: Steady-state behavior of Markov chains](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@Lec__25_Steady-state_behavior_of_Markov_chains)

Printable transcript available [here](https://courses.edx.org/assets/courseware/v1/9e3113a4f082aff3fb4aa3711ac676be/asset-v1:MITx+6.431x+1T2024+type@asset+block/transcripts_L25-Overview.pdf).

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/bf8416081e40a39d55b2ba6bc3d57f6d/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L25-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/913c3d972feb0fc895e2ac319daa716f/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L25-annotated-slides.pdf)

More information is given in [Section 7.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/55) of the text.

# [Lecture 26: Absorption probabilities and expected time to absorption (optional)](https://learning.edx.org/course/course-v1:MITx+6.431x+1T2024/block-v1:MITx+6.431x+1T2024+type@sequential+block@_Optional_Ungraded__Lec__26_Absorption_probabilities_and_expected_time_to_absorption)

In this final lecture, we first review the various properties of a Markov chain that ensure steady-state behavior and provide some insights on how good an approximation we have when we use steady-state probabilities to characterize the behavior of a Markov chain that has run for a long time, but not an infinite amount of time.

We then consider a classical application of Markov chains, which has to do with the design of a phone system.

We finally introduce the notion of absorbing states and show how to calculate the probability of ending up in such a state, as well as related quantities such as the expected time it takes to do so.

Printable transcript available [here](https://courses.edx.org/assets/courseware/v1/8cd509351ac8697330fe56e1e7665b4b/asset-v1:MITx+6.431x+1T2024+type@asset+block/transcripts_L26-Overview.pdf).

Lecture slides: [[clean]](https://courses.edx.org/assets/courseware/v1/06d601c9707367515a35f9ba65ad3f58/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L26-clean-slides.pdf) [[annotated]](https://courses.edx.org/assets/courseware/v1/80381d88b513e9dd4710f430d65a8979/asset-v1:MITx+6.431x+1T2024+type@asset+block/lectureslides_L26-annotated-slides.pdf)

More information is given in [Section 7.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2024/pdfbook/0/chapter/1/56) of the text.
elections-candidates
====================

Fun project to print out the distributions of age, star sign and genders of candidates of political parties from the 2009 general elections

example:

    ./run.sh "AFRICAN NATIONAL CONGRESS"

this returns a file called AFRICAN_NATIONAL_CONGRESS.dat" which looks like this:

    Party : AFRICAN NATIONAL CONGRESS
    Number of Candidates: 393
    ====================


    Distribution by age
    ====================

    20 - 29: 0.51%
    80 - 89: 1.02%
    30 - 39: 3.56%
    70 - 79: 11.70%
    40 - 49: 14.76%
    60 - 69: 27.48%
    50 - 59: 40.97%

    Distribution by star sign
    ====================

    Sagittarius: 6.11%
    Pisces: 6.87%
    Capricorn: 7.12%
    Scorpio: 7.63%
    Aquarius: 7.89%
    Leo: 7.89%
    Gemini: 7.89%
    Taurus: 8.91%
    Libra: 9.16%
    Virgo: 9.67%
    Aries: 9.67%
    Cancer: 11.20%

    Distribution by gender
    ====================

    Woman: 48.35%
    Man: 51.65%

Party names can be found in the candidates.pdf that is downloaded if you run:

    make candidates.pdf

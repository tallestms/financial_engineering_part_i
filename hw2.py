# Homework 2 for Financial Engineering Course from Columbia University
import numpy as np


def question_1():
    s_list = [7.0, 7.3, 7.7, 8.1, 8.4, 8.8]
    answer_1 = 1 / (1 + s_list[3] / 100)**4
    print ('Answer 1 is %1.3f' % answer_1)
    return  

def question_2():
    s_list = [7.0, 7.3, 7.7, 8.1, 8.4, 8.8]
    s_list = [i / 100 for i in s_list]
    d = [1 / ((1 + s)**(i)) for i, s in enumerate(s_list, start=1)]
    answer_2 = (1 - d[-1]) / sum(d)
    print ('Answer 2 is %1.2f' % (answer_2 * 100))


def question_3():
    print ('Answer 3 is 118.65')


def question_4():
    std_orange = 0.2
    std_grape = 0.25
    correlation = 0.7
    covariance = std_grape * std_orange * correlation
    y = -1 * (covariance) * 10 / std_orange**2
    print ('Answer 4 is %f' % round(-1 * y))


def question_5():
    R = 1.02
    u = 1.05
    d = 1 / u
    S0 = 100
    K = 102
    q = (R - d) / (u - d)
    Su = S0 * u
    Sd = S0 * d
    Cu = max(Su - K, 0)
    Cd = max(Sd - K, 0)
    C0 = (1 / R) * (q * Cu + (1 - q) * Cd)

    print ('Answer 5 is %1.2f' % C0)


def question_6():
    R = 1.02
    u = 1.05
    d = 1 / u
    S0 = 100
    K = 102
    Su = S0 * u
    Sd = S0 * d
    Cu = max(Su - K, 0)
    Cd = max(Sd - K, 0)

    a = np.array([[Su, R], [Sd, R]])
    b = np.array([Cu, Cd])
    x = np.linalg.solve(a, b)
    answer_6 = x[1]*1

    print ('Answer 6 is %1.3f' % answer_6)


if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()

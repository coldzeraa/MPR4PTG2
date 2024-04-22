package swp.basics.tests;

import swp.basics.observer.pull.Observer;
import swp.basics.observer.pull.impl.ConcreteObserver;
import swp.basics.observer.pull.impl.TimerObservable;

public class ObserverSimpleTest {

    public static void main(String[] args) throws InterruptedException {
        TimerObservable timer = new TimerObservable(10, 100);
        TimerObservable timer2 = new TimerObservable(10, 100);

        Observer obs1 = new ConcreteObserver(timer);

        timer.registerObserver(obs1);
        timer2.registerObserver(obs1);
        timer.runTimer();
        timer2.runTimer();
    }
}

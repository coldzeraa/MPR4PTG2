package swp.basics.tests;

import swp.basics.observer.push.Observer;
import swp.basics.observer.push.impl.ConcreteObserver;
import swp.basics.observer.push.impl.TimerObservable;
import swp.basics.observer.push.impl.TimerObservableObserver;

import java.util.Timer;

public class ObservableObserverTest {

    public static void main(String[] args) throws InterruptedException {
        TimerObservable timer = new TimerObservable(10, 100);
        TimerObservableObserver obsObs1 = new TimerObservableObserver(10, 100);
        TimerObservableObserver obsObs2 = new TimerObservableObserver(10, 100);
        Observer obs = new ConcreteObserver();

        timer.registerObserver(obsObs1);
        timer.registerObserver(obsObs2);
        obsObs1.registerObserver(obs);
        obsObs2.registerObserver(obs);

        timer.runTimer();

    }
}

package swp.basics.observer.push.impl;

import swp.basics.observer.push.Observable;
import swp.basics.observer.push.Observer;

public class ConcreteObserver implements Observer {

    Observable observable;

    @Override
    public void update(Observable observable, Object argument) {
        System.out.println("Update of " + this + ": " + observable + " with new state" + argument);
    }

}

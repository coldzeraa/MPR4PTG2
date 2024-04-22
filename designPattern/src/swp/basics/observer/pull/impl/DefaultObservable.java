package swp.basics.observer.pull.impl;


import swp.basics.observer.pull.Observable;
import swp.basics.observer.pull.Observer;

import java.util.HashSet;
import java.util.Set;

public abstract class DefaultObservable implements Observable {

    private Set<Observer> registeredObservers = new HashSet<>();

    @Override
    public void registerObserver(Observer observer) {
        registeredObservers.add(observer);
    }

    @Override
    public void unregisterObserver(Observer observer) {
        registeredObservers.remove(observer);
    }

    @Override
    public void notifyObserver() {
        for (Observer observer : registeredObservers)
            observer.update();
    }

    public abstract Object getState();
}

package swp.basics.observer.push;

import swp.basics.observer.push.Observer;

public interface Observable {

    void registerObserver(Observer observer);

    void unregisterObserver(Observer observer);

    void notifyObserver();
}

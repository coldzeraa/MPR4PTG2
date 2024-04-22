package swp.basics.observer.push.impl;

import swp.basics.observer.push.Observable;
import swp.basics.observer.push.impl.DefaultObservable;
import swp.basics.observer.push.Observer;

public class TimerObservableObserver extends DefaultObservable implements Observer {
    private int ticks;
    private int interval;

    public TimerObservableObserver(int ticks, int interval) {
        this.ticks = ticks;
        this.interval = interval;
    }

    public void runTimer() throws InterruptedException {
        while (ticks > 0){
            Thread.sleep(interval);
            ticks--;
            this.notifyObserver();
        }
    }

    public Object getState(){
        return ticks;
    }

    @Override
    public void update(Observable observable, Object argument) {
        System.out.println("Update of " + this + ": " + observable + " with new state" + argument);
        notifyObserver();
    }
}

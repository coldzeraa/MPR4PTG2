package swp.basics.observer.pull.impl;

import swp.basics.observer.pull.impl.DefaultObservable;

public class TimerObservable extends DefaultObservable {

    private int ticks;
    private int interval;

    public TimerObservable(int ticks, int interval) {
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

}

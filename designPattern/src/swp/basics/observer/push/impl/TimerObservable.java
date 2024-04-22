package swp.basics.observer.push.impl;

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

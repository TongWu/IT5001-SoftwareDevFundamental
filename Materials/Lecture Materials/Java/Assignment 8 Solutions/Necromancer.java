/** A necromancer */
public class Necromancer extends Mage {
    // public constants
    public static final int COST = 400;
    // private constants
    private static final String NECROMANCER_NAME = "Necromancer";
    private static final String REVIVAL_FORMAT_STRING = "Reviving %s\n";
    private static final double REVIVAL_PENALTY = 0.5;
    
    public Necromancer() {
        super(NECROMANCER_NAME);
    }

    @Override
    public void cast(Team myTeam, Team enemyTeam) {
        if (myTeam.isAllAlive())
            super.cast(myTeam, enemyTeam);
        else {
            GameCharacter target = myTeam.getRandomDeadCharacter();
            System.out.printf(REVIVAL_FORMAT_STRING, target);
            target.revive(REVIVAL_PENALTY);
        }
    }
}

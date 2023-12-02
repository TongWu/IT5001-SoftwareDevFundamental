/** An arch mage */
public class ArchMage extends Mage {
    // public constants
    public static final int COST = 600;

    // private constants
    private static final String ARCHMAGE_NAME = "ArchMage";
    private static final String KABOOM_STRING = "Cast KABOOM! Strike every enemy!";
    private static final int KABOOM_MULTIPLIER = 2;
    public ArchMage() {
        super(ARCHMAGE_NAME);
    }

    @Override
    public void cast(Team myTeam, Team enemyTeam) {
        if (myTeam.getAllLivingCharacters().length > 1) {
            super.cast(myTeam, enemyTeam);
        } else {
            System.out.println(KABOOM_STRING);
            for (GameCharacter c : enemyTeam.getAllLivingCharacters())
                c.gotHurt(intelligence * KABOOM_MULTIPLIER);
        }
    }
}

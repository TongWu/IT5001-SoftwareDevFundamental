import java.util.Random;
import java.util.Scanner;
import java.util.function.Supplier;
import java.util.stream.Stream;
public class App {
    private static final Random rng = new Random(1);
    private static final Scanner sc = new Scanner(System.in);
    private static final int STARTING_GOLD = 1000;
    private static final Triplet[] CHARACTER_SELECTION = new Triplet[]{
        // comment out the lines you do not want in your character selection
        new Triplet("Fighter", Fighter.COST, Fighter::new),
        new Triplet("Mage", Mage.COST, Mage::new),
        new Triplet("Berserker", Berserker.COST, Berserker::new),
        new Triplet("ArchMage", ArchMage.COST, ArchMage::new),
        new Triplet("Necromancer", Necromancer.COST, Necromancer::new),
    };
    private static final String USER = "USER";
    private static final String ENEMY = "ENEMY";

    public static void main(String[] args) {
        Team enemy = createRandomTeam();
        Team user = userChooseTeam();
        String winner = runBattle(user, enemy, USER);
        System.out.printf("%s wins!\n", winner);
    }

    private static String runBattle(Team user, Team enemy, String turn) {
        printGameConfiguration(user, enemy);
        System.out.printf("%s's turn\n", turn);
        if (user.isAllDead()) return ENEMY;
        if (enemy.isAllDead()) return USER;
        if (turn.equals(USER)) {
            // let user select a character that is alive
            GameCharacter[] availableCharacters = user.getAllLivingCharacters();
            for (int i = 0; i < availableCharacters.length; ++i)
                System.out.printf("%d: %s\n", i, availableCharacters[i]);
            int selection = safeReadInt("Choose a character to act...", 0, availableCharacters.length);
            availableCharacters[selection].act(user, enemy);
            return runBattle(user, enemy, ENEMY);
        }
        enemy.getRandomLivingCharacter().act(enemy, user);
        return runBattle(user, enemy, USER);
    }

    private static Team createRandomTeam() {
        return createRandomTeam(STARTING_GOLD, new Team(rng));
    }

    private static Team createRandomTeam(int gold, Team t) {
        Triplet[] availableCharacters = getAvailableCharacters(gold);
        if (availableCharacters.length == 0)
            return t;
        Triplet selection = availableCharacters[rng.nextInt(availableCharacters.length)];
        t.addMember(selection.third.get());
        return createRandomTeam(gold - selection.second, t);
    }

    private static Team userChooseTeam() {
        return userChooseTeam(STARTING_GOLD, new Team(rng));
    }

    private static Team userChooseTeam(int gold, Team t) {
        Triplet[] availableCharacters = getAvailableCharacters(gold);
        if (availableCharacters.length == 0) return t;
        System.out.printf("You have %d gold left\n", gold);
        for (int i = 0; i < availableCharacters.length; ++i)
            System.out.printf("%d: %s (%d gold)\n", i, availableCharacters[i].first, availableCharacters[i].second);        
        int selection = safeReadInt("Please enter your chosen character... ", 0, availableCharacters.length);
        Triplet tt = availableCharacters[selection];
        t.addMember(tt.third.get());
        return userChooseTeam(gold - tt.second, t);
    }

    private static int safeReadInt(String msg, int low, int high) {
        System.out.printf(msg);
        try {
            int res = sc.nextInt();
            if (low <= res && res < high)
                return res;
            else
                throw new RuntimeException("not a valid selection!");
        } catch (Exception e) {
            System.out.println("Please enter a valid selection");
            return safeReadInt(msg, low, high);
        }
    }

    private static void printGameConfiguration(Team user, Team enemy) {
        System.out.println("=== Enemy Team ===");
        System.out.println(enemy);
        System.out.println("=== Your Team ===");
        System.out.println(user);
    }

    private static Triplet[] getAvailableCharacters(int gold) {
        return Stream.of(CHARACTER_SELECTION)
            .filter(x -> x.second <= gold)
            .toArray(Triplet[]::new);
    }

    private static class Triplet {
        String first;
        Integer second;
        Supplier<GameCharacter> third;
        Triplet(String first, int second, Supplier<GameCharacter> third) {
            this.first = first;
            this.second = second;
            this.third = third;
        }
    }
}

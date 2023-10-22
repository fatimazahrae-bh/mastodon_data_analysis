import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.json.JSONObject;

public class TootsMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    private Text outputKey = new Text();
    private LongWritable followersCount = new LongWritable();

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        try {
            // Charger la ligne JSON
            String line = value.toString();
            JSONObject toot = new JSONObject(line);

            // Extraction des informations de l'utilisateur
            JSONObject user = toot.getJSONObject("account");
            String username = user.getString("username");
            long followers = user.getLong("followers_count");

            // Émettre le nom d'utilisateur et le nombre de followers
            outputKey.set(username);
            followersCount.set(followers);
            context.write(outputKey, followersCount);
        } catch (Exception e) {
            // Gérer les erreurs de lecture des toots
            System.err.println("Error processing toot: " + e.getMessage());
        }
    }
}


import csv
from datetime import datetime, timedelta
import pytz  # For handling timezones

def generate_alice_csv():
    """
    Generates a CSV file with Alice in Wonderland short story prompts
    with specific date and numbering formats.
    """
    start_date_str = "2025-03-29"
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    start_time = datetime.strptime("18:00", "%H:%M").time()
    pst_timezone = pytz.timezone('America/Los_Angeles')

    output_filename = "alice_wonderland_shorts.csv"
    fieldnames = ["Date_Time", "Prompt"]

    with open(output_filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        current_count = 61
        current_date = start_date

        while current_count <= 960:
            # Determine the day of the week (0=Monday, 6=Sunday)
            day_of_week = current_date.weekday()

            # Check if the current day is Thursday (3), Friday (4), Saturday (5), or Sunday (6)
            if day_of_week in [3, 4, 5, 6]:
                for i in range(10):
                    if current_count > 960:
                        break

                    combined_datetime = datetime.combine(current_date, start_time)
                    pst_datetime = pst_timezone.localize(combined_datetime)
                    formatted_datetime = pst_datetime.strftime("%m/%d/%Y %H:%M")

                    prompt = f"Alice's Adventures in Wonderland - {current_count} (10 Second Short) 🐰✨ WONDERLAND AWAITS! Watch Alice's next adventure unfold! 🎩🫖 🎭 Curious characters! Impossible things! Magic around every corner! 🎧 Get the FULL audiobook: [Audible Link Coming Soon!] 📚 OWN THE CLASSIC: 👉 Paperback: https://www.amazon.com/dp/B0F1LYQVXM 👉 Hardcover: https://www.amazon.com/dp/B0F1LW9L59 👉 Kindle eBook: https://www.amazon.com/dp/B0F1KW134R 🔮 Down the rabbit hole we go! Follow for daily Wonderland magic! ✨ 💭 Tag someone who needs a little Wonderland in their life! 🍄 #AliceInWonderland #BookTok #ClassicBooks #Wonderland #ShortStories #Audiobook"
                    writer.writerow([formatted_datetime, prompt])
                    current_count += 1

            # Move to the next day
            current_date += timedelta(days=1)

if __name__ == "__main__":
    generate_alice_csv()
    print("CSV file 'alice_wonderland_shorts.csv' has been created successfully.")

import gradio as gr


def merge_sort(playlist, key, increasing=True):
    if len(playlist) <= 1:
        return playlist

    mid = len(playlist) // 2
    left = merge_sort(playlist[:mid], key, increasing)
    right = merge_sort(playlist[mid:], key, increasing)

    return merge(left, right, key, increasing)


def merge(left, right, key, increasing):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_val = left[i][key]
        right_val = right[j][key]

        if increasing:
            if left_val <= right_val:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left_val >= right_val:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def parse_playlist(song_text):
    playlist = []

    if not song_text.strip():
        return [], "Error: please enter at least one song."

    lines = song_text.strip().split("\n")

    for line_number, line in enumerate(lines, start=1):
        parts = [part.strip() for part in line.split(",")]

        if len(parts) != 4:
            return [], f"Error on line {line_number}: each line must have title, artist, energy, duration."

        title, artist, energy, duration = parts

        try:
            energy = int(energy)
            duration = int(duration)
        except ValueError:
            return [], f"Error on line {line_number}: energy and duration must be numbers."

        if energy < 0 or energy > 100:
            return [], f"Error on line {line_number}: energy must be between 0 and 100."

        if duration < 0:
            return [], f"Error on line {line_number}: duration must be 0 or greater."

        song = {
            "title": title,
            "artist": artist,
            "energy": energy,
            "duration": duration
        }

        playlist.append(song)

    return playlist, None


def format_playlist(playlist):
    output_lines = []

    for song in playlist:
        line = (
            f"Title: {song['title']} | "
            f"Artist: {song['artist']} | "
            f"Energy: {song['energy']} | "
            f"Duration: {song['duration']}"
        )
        output_lines.append(line)

    return "\n".join(output_lines)


def sort_playlist(song_text, category, order):
    playlist, error = parse_playlist(song_text)

    if error:
        return error

    increasing = True if order == "increasing" else False
    sorted_playlist = merge_sort(playlist, category, increasing)

    return format_playlist(sorted_playlist)


with gr.Blocks() as demo:
    gr.Markdown("# Playlist Vibe Builder")
    gr.Markdown(
        "Enter one song per line in this format:\n"
        "`title, artist, energy, duration`"
    )

    song_input = gr.Textbox(
        label="Songs",
        lines=10,
        placeholder="Pacific, Chase Petra, 60, 200"
    )

    category_input = gr.Dropdown(
        choices=["title", "artist", "energy", "duration"],
        label="Sorting Category",
        value="energy"
    )

    order_input = gr.Dropdown(
        choices=["increasing", "decreasing"],
        label="Sorting Order",
        value="increasing"
    )

    sort_button = gr.Button("Sort Playlist")

    output_box = gr.Textbox(
        label="Sorted Playlist",
        lines=12
    )

    sort_button.click(
        fn=sort_playlist,
        inputs=[song_input, category_input, order_input],
        outputs=output_box
    )

demo.launch()

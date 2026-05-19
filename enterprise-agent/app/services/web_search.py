from ddgs import DDGS


def search_web(query):

    results_text = ""

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")

            results_text += f"""
Title: {title}
Content: {body}

"""

    return results_text
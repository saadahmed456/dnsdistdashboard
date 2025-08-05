import requests

def fetch_top_queries(dnsdist_host, api_key):
    url = f"http://{dnsdist_host}/jsonstat"
    headers = {"X-API-Key": api_key}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return {"server": dnsdist_host, "top_queries": response.json().get("TopQueries", [])}
    except Exception as e:
        return {"server": dnsdist_host, "error": str(e)}

def fetch_all_top_queries(servers):
    return [fetch_top_queries(s["host"], s["api_key"]) for s in servers]

from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return render(request, "index.html")


def get_contributions_data(request, username):
    url = "https://api.github.com/graphql"
    token = "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"
    headers = {"Authorization": f"Bearer {token}"}
    body = f"""
    {{
      user(login: "{username}") {{
        contributionsCollection {{
          contributionCalendar {{
            weeks {{
              contributionDays {{
                color
              }}
            }}
          }}
        }}
      }}
    }}
    """
    response = requests.post(url, json={"query": body}, headers=headers)
    return HttpResponse(response.content if response.status_code == 200 else response.reason)

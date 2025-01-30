from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return render(request, "index.html")


def get_contributions_data(request, username, access_token = None):
    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {access_token}"}
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
    response = requests.post(url, json={"query": body}, headers=headers if access_token else None)
    if response.status_code == 200:
        calender = response.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        calender["weeks"] = calender["weeks"][::-1]
        return render(request, "trak_chart.html", calender)
    else:
        return HttpResponse(f"""status code: {response.status_code} reson: {response.reason} content: {response.content}""")

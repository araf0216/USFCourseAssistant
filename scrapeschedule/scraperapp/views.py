import subprocess
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'scraperapp/index.html')

@csrf_exempt
def scrape(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        crn = data.get('input', '')

        result = subprocess.run(["python", "../testing/scrape_course.py", crn], capture_output=True, text=True)
        
        # out = json.loads(result.stdout)

        # print(out["result"])

        # Check for errors
        # if result.returncode != 0:
        #     return JsonResponse({'error': 'Script failed', 'details': result.stderr}, status=500)
        # else:
        #     # Parse the JSON output from the script
        #     try:
        #         output = json.loads(result.stdout.strip())
        #     except json.JSONDecodeError:
        #         return JsonResponse({'error': 'Invalid JSON returned'}, status=500)
            
        #     return JsonResponse(output)

        return JsonResponse({"message": result.stdout.strip()})
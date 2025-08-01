from django.shortcuts import render, redirect
from .utils import fetch_case_data
from .models import CaseQueryLog

def case_lookup(request):
    if request.method == "POST":
        case_type = request.POST.get("case_type", "").strip()
        case_number = request.POST.get("case_number", "").strip()
        filing_year = request.POST.get("filing_year", "").strip()

        if not (case_type and case_number and filing_year):
            request.session['error'] = "Please fill in all fields."
            return redirect('case_lookup')

        try:
            result = fetch_case_data(case_type, case_number, filing_year)

            # Save to DB only if result is valid
            CaseQueryLog.objects.create(
                case_type=case_type,
                case_number=case_number,
                filing_year=int(filing_year),
                status=result.get("status", "failed"),
                error_message=result.get("error", ""),
                raw_response=str(result)
            )

            
            request.session['result'] = result

        except Exception as e:
            request.session['error'] = f"Unexpected error occurred: {str(e)}"

        return redirect('case_lookup')   

     
    context = {}
    if 'error' in request.session:
        context['error'] = request.session.pop('error')   
    if 'result' in request.session:
        context['result'] = request.session.pop('result')   

    return render(request, "index.html", context)

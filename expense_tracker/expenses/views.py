from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

# ✅ Add Expense
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # ✅ Must link to logged-in user
            expense.save()
            return redirect('all_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})


@login_required
def all_expenses(request):
    expenses = Expense.objects.filter(user=request.user)  # or just Expense.objects.all()
    return render(request, 'expenses/all_expense.html', {'expenses': expenses})


def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('all_expenses')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/edit_expense.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':
        expense.delete()
        return redirect('all_expenses')

    return render(request, 'expenses/delete_expense.html', {'expense': expense})

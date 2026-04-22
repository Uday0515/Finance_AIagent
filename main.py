from pydantic import BaseModel, Field
from typing import List, Optional


class SpendingCategory(BaseModel):
    category: str
    amount: float
    percentage: Optional[float] = None


class BudgetAnalysis(BaseModel):
    total_expenses: float
    monthly_income: Optional[float] = None
    spending_categories: List[SpendingCategory]


class EmergencyFund(BaseModel):
    recommended_amount: float
    current_status: str


class SavingsStrategy(BaseModel):
    emergency_fund: EmergencyFund
    monthly_savings_target: float


class Debt(BaseModel):
    name: str
    amount: float
    interest_rate: float
    min_payment: Optional[float] = None


class DebtReduction(BaseModel):
    total_debt: float
    debts: List[Debt]
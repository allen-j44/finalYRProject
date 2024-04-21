// player.model.ts
export interface Player {
    _id: string;
    Team: string;
    Name: string;
    Age: number;
    POS: string;
    App: number;
    GoalInvolvements: number;
    CleanSheets: number;
    Yellows: number;
    Reds: number;
    Mins: number;
  }
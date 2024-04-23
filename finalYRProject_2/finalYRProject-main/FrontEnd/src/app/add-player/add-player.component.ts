import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-add-player',
  templateUrl: './add-player.component.html',
  styleUrl: './add-player.component.scss'
})

export class AddPlayerComponent   {
  public Age: any;
  public Yellows: any;
  public Team: any;
  public Reds: any;
  public POS: any;
  public Name: any;
  public Mins: any;
  public App: any;
  public Goal: any;
  public Clean: any;

  constructor(private api: ApiService){}

  AddPlayer(){
    const player = {
      age: this.Age,
      yellows: this.Yellows,
      team: this.Team,
      reds: this.Reds,
      pos: this.POS,
      name: this.Name,
      mins: this.Mins,
      app: this.App,
      goal: this.Goal,
      clean: this.Clean
    }
    this.api.AddPlayer(player).subscribe((data: any) => {
      console.log(data);
    });
  }
}

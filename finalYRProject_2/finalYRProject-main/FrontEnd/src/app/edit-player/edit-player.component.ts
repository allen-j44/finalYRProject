import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-edit-player',
  templateUrl: './edit-player.component.html',
  styleUrl: './edit-player.component.scss'
})
export class EditPlayerComponent implements OnInit {

  public player: any;

  constructor(private route: ActivatedRoute, private api: ApiService){}


  ngOnInit(): void {
    this.route.paramMap.subscribe((params:any) => {
      const playerId = params.get('id');
      console.log(playerId);
      this.api.GetOnePlayer(playerId).subscribe((data:any) => {
        this.player = data;
      })
      // Now you can use productId in your component logic
    });
  }

  SavePlayer(){
    this.api.SavePlayer(this.player).subscribe((data: any) => {
      console.log(data);
    });
  }
}

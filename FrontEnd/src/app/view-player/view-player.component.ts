import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-view-player',
  templateUrl: './view-player.component.html',
  styleUrl: './view-player.component.scss'
})
export class ViewPlayerComponent implements OnInit {

  public playerId: any;
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
}

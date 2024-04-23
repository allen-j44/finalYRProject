import { Component, OnInit } from '@angular/core';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-get-player',
  templateUrl: './get-player.component.html',
  styleUrl: './get-player.component.scss'
})
export class GetPlayerComponent implements OnInit {



  public players : any = [];
  public searchString: any;

  constructor(private api: ApiService){}
  ngOnInit(): void {
    this.api.GetPlayer().subscribe((data) => {
      this.players = data;
    });
  }

  delete(id: any){
    console.log(id);
    this.players = this.players.filter((p: any) => p._id !== id);
    this.api.Delete(id).subscribe((data) => {
      console.log(data);
    });
    }


    Search() {
      this.api.GetPlayerByName(this.searchString).subscribe((data) => {
        
        console.log(data);
        this.players = [];
        this.players.push(data);
        
      });
      }

      ClearSearch() {
      this.searchString = "";
      this.api.GetPlayer().subscribe((data) => {
        this.players = data;
      });
      }
    }
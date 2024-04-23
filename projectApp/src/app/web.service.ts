import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
@Injectable({providedIn: 'root'})
export class WebService {



  constructor(private http: HttpClient) {}

  /* Function to using the url which links to my back-end code*/
  

  getPlayers(page: number) {
    return this.http.get('http://127.0.0.1:5000/api/v1.0/players?pn=' +
                          page);

  }

  /* Function to Get an Individual Player from the dataset using the url which links to my back-end code*/

  getPlayer(id: any) {
    return this.http.get('http://127.0.0.1:5000/api/v1.0/players/' + id);

  }

  /* Function to Add a New Player to the dataset using the url which links to my back-end code*/

  postPlayer(playerData: any){
    return this.http.post(`http://127.0.0.1:5000/api/v1.0/players`, playerData);
  }

  /* Function to Get Managers Comements from a player using the url which links to my back-end code*/

  getmanagersComments(id: any) {
    return this.http.get('http://127.0.0.1:5000/api/v1.0/players/' + id +
                          '/comments');

  }

  /* Function to Post a new player to the dataset using the url which links to my back-end code*/

  postComment(playerId: string, comment: any){
      return this.http.post(`http://127.0.0.1:5000/api/v1.0/players/${playerId}/comments`, comment);
  }

  /* Function to Delete a Player from the dataset using the url which links to my back-end code*/

  deletePlayer(playerId: string) {
     return this.http.delete(`http://127.0.0.1:5000/api/v1.0/players/${playerId}`).subscribe((data: any) => {
       return this.getPlayers(1);
     });
  }
}

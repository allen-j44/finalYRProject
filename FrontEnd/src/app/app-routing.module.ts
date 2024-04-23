import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GetPlayerComponent } from './get-player/get-player.component';
import { ViewPlayerComponent } from './view-player/view-player.component';
import { EditPlayerComponent } from './edit-player/edit-player.component';
import { AddPlayerComponent } from './add-player/add-player.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: GetPlayerComponent},
  {path: 'player/:id', component: ViewPlayerComponent},
  {path: 'player/:id/edit', component: EditPlayerComponent},
  {path: 'add', component: AddPlayerComponent},
  {path: 'login', component: LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

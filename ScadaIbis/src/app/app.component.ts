import { CommonModule } from '@angular/common';
import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'ScadaIbis';
  public airConditon1 : boolean = false
  public light1 : boolean = false
  public heater1 : boolean = false
  public alarm1 : boolean = false
  public ventilation1 : boolean = false

  public airConditon2 : boolean = false
  public light2 : boolean = false
  public heater2 : boolean = false
  public alarm2 : boolean = false
  public ventilation2 : boolean = false

  public airConditon3 : boolean = false
  public light3 : boolean = false
  public heater3 : boolean = false
  public alarm3 : boolean = false
  public ventilation3 : boolean = false

  public airConditon4 : boolean = false
  public light4 : boolean = false
  public heater4 : boolean = false
  public alarm4 : boolean = false
  public ventilation4 : boolean = false

  public airConditon5 : boolean = false
  public light5 : boolean = false
  public heater5 : boolean = false
  public alarm5 : boolean = false
  public ventilation5 : boolean = false
  
  public airConditon6 : boolean = false
  public light6 : boolean = false
  public heater6 : boolean = false
  public alarm6 : boolean = false
  public ventilation6 : boolean = false
}

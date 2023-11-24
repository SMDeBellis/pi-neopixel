import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ColorMatrixComponent } from './color-matrix.component';

describe('ColorMatrixComponent', () => {
  let component: ColorMatrixComponent;
  let fixture: ComponentFixture<ColorMatrixComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ColorMatrixComponent]
    });
    fixture = TestBed.createComponent(ColorMatrixComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

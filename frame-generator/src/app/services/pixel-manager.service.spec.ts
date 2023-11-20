import { TestBed } from '@angular/core/testing';

import { PixelManagerService } from './pixel-manager.service';

describe('PixelManagerService', () => {
  let service: PixelManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PixelManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

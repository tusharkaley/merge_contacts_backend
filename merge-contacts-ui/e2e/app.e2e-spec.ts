import { MergeContactsUiPage } from './app.po';

describe('merge-contacts-ui App', () => {
  let page: MergeContactsUiPage;

  beforeEach(() => {
    page = new MergeContactsUiPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});

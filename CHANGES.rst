Changelog
=========

1.0.3 (unreleased)
------------------

New:

- *add item here*

Fixes:

- Changed i18n_domain to "plone"
  [claytonc]


1.0.2 (2015-09-09)
------------------

- Remove superfluous 'for'.
  [fulv]

- Fix tests: redirect was changed in commit e7367258.
  [jone]

- If the content is locked, the redirect points to the default view and
  not to the absolute_url of the object. It avoids image opening on redirect
  [parruc]


1.0.1 (2011-12-06)
------------------

- Fix version requirement of plone.dexterity: 1.1 is compatible.
  [jone]


1.0 (2011-11-27)
----------------

- Fixed problem: locks were not released when editing content and saving
  it without changing anything. Fixed by using new IEditFinishedEvent instead
  of IObjectModifiedEvent.
  [jbaumann]

- Fixed problem which caused widget traversal to fail.
  The edit form is now protected for non-anonymous user, since locking for
  anyonmous users does not work anyway.
  [jbaumann]

- Initial implementation
  [jbaumann]

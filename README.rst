Class for use https://instagram.com

=======
Install
=======

.. code-block:: bash

    pip install instagram

=======
Example
=======

.. code-block:: python

    from instagramAPI import instagramAPI

    access_token = '3403089465.260c1aa.b09a16*03c24435880d3fe195*f8f156

    instagram = instagramAPI(access_token)

    print instagram.users_self()

    print instagram.users_detail(3403089465)

    print instagram.users_self_media_liked()

    print instagram.followed_by()

    print instagram.follows_self()

    print instagram.media_self_recent()

    print instagram.media('1306717096452924663_3403089465')

=======
License
=======

MIT

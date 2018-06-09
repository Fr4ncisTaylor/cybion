# -*- coding,utf-8 -*-

import utils, json


def check_out(params, lists):
	p = []
	p.append(params)
	for item in p:
		if item in lists:
			pass
		else:
			print('Unknow item %s' %s(item))


def make_inline(**args):
	json_dicts = json.dumps(args)
	return json_dicts
  
"""
WebhookInfo = {'WebhookInfo', 
                  'url',
                  'has_custom_certificate',
                  'pending_update_count',
                  'last_error_date',
                  'last_error_message',
              }

#-end-#
InputTextMessageContent = {'InputTextMessageContent', 
                              'message_text',
                              'parse_mode',
                              'disable_web_page_preview',
                          }

#-end-#
InputLocationMessageContent = {'InputLocationMessageContent', 
                                  'latitude',
                                  'longitude',
                                  'live_period',
                              }

#-end-#
InputVenueMessageContent = {'InputVenueMessageContent', 
                               'latitude',
                               'longitude',
                               'title',
                               'address',
                               'foursquare_id',
                           }

#-end-#
InputContactMessageContent = {'InputContactMessageContent', 
                                 'phone_number',
                                 'first_name',
                                 'last_name',
                             }

#-end-#
InlineQueryResultArticle = {'InlineQueryResultArticle', 
                               {'type', 'default','article'},
                               'id',
                               'title',
                               'input_message_content',
                               'reply_markup',
                               'url',
                               'hide_url',
                               'description',
                               'thumb_url',
                               'thumb_width',
                               'thumb_height',
                           }

#-end-#
InlineQueryResultPhoto = {'InlineQueryResultPhoto', 
                             {'type', 'default','photo'},
                             'id',
                             'photo_url',
                             'thumb_url',
                             'photo_width',
                             'photo_height',
                             'title',
                             'description',
                             'caption',
                             'parse_mode',
                             'reply_markup',
                             'input_message_content',
                         }

#-end-#
InlineQueryResultGif = {'InlineQueryResultGif', 
                           {'type', 'default','gif'},
                           'id',
                           'gif_url',
                           'gif_width',
                           'gif_height',
                           'gif_duration',
                           'thumb_url',
                           'title',
                           'caption',
                           'parse_mode',
                           'reply_markup',
                           'input_message_content',
                       }

#-end-#
InlineQueryResultMpeg4Gif = {'InlineQueryResultMpeg4Gif', 
                                {'type', 'default','mpeg4_gif'},
                                'id',
                                'mpeg4_url',
                                'mpeg4_width',
                                'mpeg4_height',
                                'mpeg4_duration',
                                'thumb_url',
                                'title',
                                'caption',
                                'parse_mode',
                                'reply_markup',
                                'input_message_content',
                            }

#-end-#
InlineQueryResultVideo = {'InlineQueryResultVideo', 
                             {'type', 'default','video'},
                             'id',
                             'video_url',
                             'mime_type',
                             'thumb_url',
                             'title',
                             'caption',
                             'parse_mode',
                             'video_width',
                             'video_height',
                             'video_duration',
                             'description',
                             'reply_markup',
                             'input_message_content',
                         }

#-end-#
InlineQueryResultAudio = {'InlineQueryResultAudio', 
                             {'type', 'default','audio'},
                             'id',
                             'audio_url',
                             'title',
                             'caption',
                             'parse_mode',
                             'performer',
                             'audio_duration',
                             'reply_markup',
                             'input_message_content',
                         }

#-end-#
InlineQueryResultVoice = {'InlineQueryResultVoice', 
                             {'type', 'default','voice'},
                             'id',
                             'voice_url',
                             'title',
                             'caption',
                             'parse_mode',
                             'voice_duration',
                             'reply_markup',
                             'input_message_content',
                         }

#-end-#
InlineQueryResultDocument = {'InlineQueryResultDocument', 
                                {'type', 'default','document'},
                                'id',
                                'title',
                                'caption',
                                'parse_mode',
                                'document_url',
                                'mime_type',
                                'description',
                                'reply_markup',
                                'input_message_content',
                                'thumb_url',
                                'thumb_width',
                                'thumb_height',
                            }

#-end-#
InlineQueryResultLocation = {'InlineQueryResultLocation', 
                                {'type', 'default','location'},
                                'id',
                                'latitude',
                                'longitude',
                                'title',
                                'live_period',
                                'reply_markup',
                                'input_message_content',
                                'thumb_url',
                                'thumb_width',
                                'thumb_height',
                            }

#-end-#
InlineQueryResultVenue = {'InlineQueryResultVenue', 
                                {'type', 'default','venue'},
                                'id',
                                'latitude',
                                'longitude',
                                'title',
                                'address',
                                'foursquare_id',
                                'reply_markup',
                                'input_message_content',
                                'thumb_url',
                                'thumb_width',
                                'thumb_height',
                         }

#-end-#
InlineQueryResultContact = {'InlineQueryResultContact', 
                                {'type', 'default','contact'},
                                'id',
                                'phone_number',
                                'first_name',
                                'last_name',
                                'reply_markup',
                                'input_message_content',
                                'thumb_url',
                                'thumb_width',
                                'thumb_height',
                           }

#-end-#
InlineQueryResultGame = {'InlineQueryResultGame', 
                            {'type', 'default','game'},
                            'id',
                            'game_short_name',
                            'reply_markup',
                        }

#-end-#
InlineQueryResultCachedPhoto = {'InlineQueryResultCachedPhoto', 
                                   {'type', 'default','photo'},
                                   'id',
                                   'photo_file_id',
                                   'title',
                                   'description',
                                   'caption',
                                   'parse_mode',
                                   'reply_markup',
                                   'input_message_content',
                               }

#-end-#
InlineQueryResultCachedGif = {'InlineQueryResultCachedGif', 
                                 {'type', 'default','gif'},
                                 'id',
                                 'gif_file_id',
                                 'title',
                                 'caption',
                                 'parse_mode',
                                 'reply_markup',
                                 'input_message_content',
                             }

#-end-#
InlineQueryResultCachedMpeg4Gif = {'InlineQueryResultCachedMpeg4Gif', 
                                      {'type', 'default','mpeg4_gif'},
                                      'id',
                                      'mpeg4_file_id',
                                      'title',
                                      'caption',
                                      'parse_mode',
                                      'reply_markup',
                                      'input_message_content',
                                  }

#-end-#
InlineQueryResultCachedSticker = {'InlineQueryResultCachedSticker', 
                                     {'type', 'default','sticker'},
                                     'id',
                                     'sticker_file_id',
                                     'reply_markup',
                                     'input_message_content',
                                 }

#-end-#
InlineQueryResultCachedDocument = {'InlineQueryResultCachedDocument', 
                                      {'type', 'default','document'},
                                      'id',
                                      'title',
                                      'document_file_id',
                                      'description',
                                      'caption',
                                      'parse_mode',
                                      'reply_markup',
                                      'input_message_content',
                                  }

#-end-#
InlineQueryResultCachedVideo = {'InlineQueryResultCachedVideo', 
                                   {'type', 'default','video'},
                                   'id',
                                   'video_file_id',
                                   'title',
                                   'description',
                                   'caption',
                                   'parse_mode',
                                   'reply_markup',
                                   'input_message_content',
                               }

#-end-#
InlineQueryResultCachedVoice = {'InlineQueryResultCachedVoice', 
                                   {'type', 'default','voice'},
                                   'id',
                                   'voice_file_id',
                                   'title',
                                   'caption',
                                   'parse_mode',
                                   'reply_markup',
                                   'input_message_content',
                               }

#-end-#
InlineQueryResultCachedAudio = {'InlineQueryResultCachedAudio', 
                                   {'type', 'default','audio'},
                                   'id',
                                   'audio_file_id',
                                   'caption',
                                   'parse_mode',
                                   'reply_markup',
                                   'input_message_content',
                               }

#-end-#
InputMediaPhoto = {'InputMediaPhoto', 
                      {'type', 'default','photo'},
                      'media',
                      'caption',
                      'parse_mode',
                  }

#-end-#
InputMediaVideo = {'InputMediaVideo', 
                      {'type', 'default','video'},
                      'media',
                      'caption',
                      'parse_mode',
                      'width',
                      'height',
                      'duration',
                      'supports_streaming',
                  }

# incoming
ResponseParameters = {'ResponseParameters', 
                         'migrate_to_chat_id',
                         'retry_after',
                     }

"""
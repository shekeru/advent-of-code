module Main where

import Prelude (Unit, bind, (<$>), (=<<))
import Effect (Effect)
import Effect.Console (log)
import Data.Maybe (Maybe(..))

import Web.DOM.Element (toNode)
import Web.DOM.Node (setTextContent)
import Web.DOM.NonElementParentNode (getElementById)

import Web.HTML (window)
import Web.HTML.Window (document)
import Web.HTML.HTMLDocument (toNonElementParentNode)

main :: Effect Unit
main = do
  html <- toNonElementParentNode <$> (document =<< window)
  output <- getElementById "output" html
  case toNode <$> output of
    Nothing -> log "Hello World"
    Just node -> setTextContent
      "fuck it to hell" node
